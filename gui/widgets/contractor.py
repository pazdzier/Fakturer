"""
    ..uml::
        @startuml
        @startsalt
        {+.|Dialog
        --| *           |*                     |*|*
        . |Nazwa        |"                    "|*|*
        . |NIP          |"                    "|*|*
        . |Ulica        |"                    "|*|*
        . |Miasto       |"                    "|*|*
        . |Kod pocztowy |"                    "|*|*
        . |.            | . |*|*
        . |[X] Domyślny Kontrahent | *  |*|.
        . |.            | [OK]  | [Cancel] | *

        }
        @endsaltBob
        @enduml

"""

from PySide2.QtWidgets import QWidget, QMessageBox
from database.models import Contractor
from gui.designer.add_edit_contractor import Ui_Dialog
from utils.string_validators import zip_code_validator, nip_validator


class ContractorDialog(QWidget, Ui_Dialog):

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
        self.setWindowTitle('Dodaj nowego kontrahenta')
        if self.parent.CHOSEN_CONTRACTOR:
            self.setWindowTitle('Edytuj istniejący rekord')
            self.populate_data()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def populate_data(self):

        contractor = self.parent.CHOSEN_CONTRACTOR
        self.company_name.setText(contractor.company_name)
        self.nip.setText(contractor.nip)
        self.street.setText(contractor.street)
        self.city.setText(contractor.city)
        self.zip_code.setText(contractor.zip_code)
        self.checkBox.setChecked(contractor.default)

    def accept(self):
        """ Dodaje/Edytuje kontrahenta do bazy danych """

        company_name = self.company_name.text()
        nip = nip_validator(self.nip.text())
        street = self.street.text()
        city = self.city.text()
        zip_code = zip_code_validator(self.zip_code.text())

        if not all([company_name, nip, street, city, zip_code]):
            title = "Błąd"
            message = "Pola nie mogą być puste"
            QMessageBox.warning(self, title, message)
            return

        if isinstance(nip, tuple):
            title, message = nip
            QMessageBox.warning(self, title, message)
            return

        if isinstance(zip_code, tuple):
            title, message = zip_code
            QMessageBox.warning(self, title, message)
            return

        contractor = Contractor(
            company_name=company_name,
            nip=nip,
            street=street,
            city=city,
            zip_code=zip_code,
            default=self.checkBox.isChecked(),
        )

        if self.parent.CHOSEN_CONTRACTOR:
            self.parent.CHOSEN_CONTRACTOR.deleted = True
            self.parent.CHOSEN_CONTRACTOR.default = False

        else:
            self.parent.session.query(Contractor).update({Contractor.default: False})

        self.parent.session.add(contractor)
        self.parent.session.commit()
        self.parent.populate_contractors()
        self.close()

        return

    def reject(self):

        self.close()
