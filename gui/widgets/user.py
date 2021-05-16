from sqlalchemy.sql.expression import desc
from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator
from PySide2.QtWidgets import QWidget, QMessageBox
from database.models import User
from utils.string_validators import bank_account_validator, nip_validator
from gui.designer.add_edit_user import Ui_Dialog


class UserDialog(QWidget, Ui_Dialog):

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
        self.populate_data()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        reg_ex = QRegExp(r"[\d{9}\s]*")
        input_validator = QRegExpValidator(reg_ex, self.account_number)
        self.account_number.setValidator(input_validator)

    def populate_data(self):

        try:
            user = self.parent.session.query(User).order_by(desc("id")).first()
            self.first_name.setText(user.first_name),
            self.last_name.setText(user.last_name),
            self.company_name.setText(user.company_name),
            self.street.setText(user.street),
            self.city.setText(user.city),
            self.zip_code.setText(user.zip_code),
            self.nip.setText(user.nip),
            self.account_number.setText(user.account_number.strip())
        except AttributeError:  # User records does not exist in db
            pass

    def accept(self):

        first_name = self.first_name.text()
        last_name = self.last_name.text()
        company_name = self.company_name.text()
        street = self.street.text()
        city = self.city.text()
        zip_code = self.zip_code.text()
        nip = nip_validator(self.nip.text())

        if not nip:
            QMessageBox.warning(
                self,
                "Błąd",
                f"Wartość {self.nip.text()} jest nieprawidłowa dla pola NIP",
            )
            return
        account_number = bank_account_validator(self.account_number.text())

        if not account_number:
            QMessageBox.warning(
                self,
                "Błąd",
                f"Wartość {self.account_number.text()} jest nieprawidłowa dla pola Konto bankowe",
            )
            return

        if not all(
            [first_name, last_name, company_name, street, zip_code, nip, account_number]
        ):
            QMessageBox.warning(self, "Błąd", "Pola nie mogą być puste")
            return
        user = User(
            first_name=first_name,
            last_name=last_name,
            company_name=company_name,
            street=street,
            city=city,
            zip_code=zip_code,
            nip=nip,
            account_number=account_number,
        )
        self.parent.session.add(user)
        self.parent.session.commit()
        self.close()
        return

    def reject(self):
        self.close()
