from PySide6.QtCore import QObject, SIGNAL
from PySide6.QtWidgets import QWidget
from database.models import Service
from gui.designer.services import Ui_Dialog


class ServicesDialog(QWidget, Ui_Dialog):
    def __init__(self, parent=None, edit_record=False):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
        QObject.connect(self.serviceEdit, SIGNAL("textChanged()"), self.txt_input_changed)
        if edit_record:
            self.setWindowTitle('Edytuj istniejący rekord')
            self.populate_data()
        else:
            self.setWindowTitle('Dodaj nową usługę')
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def populate_data(self):

        service = self.parent.CHOSEN_SERVICE
        self.serviceEdit.insertPlainText(service.name)
        self.amountBox.setValue(service.amount)
        self.percentageBox.setCurrentIndex(self.percentageBox.findText(service.percentage))
        
    def txt_input_changed(self):
        def characters_left():
            result = 160 - int(len(self.serviceEdit.toPlainText()))
            return str(result)

        chr_left = characters_left()
        self.char_limit.setText(chr_left)
        if int(chr_left) < 0:
            text = self.serviceEdit.toPlainText()[:159]
            self.serviceEdit.setPlainText(text)

    def accept(self):

        service = Service(
            name=self.serviceEdit.toPlainText(),
            amount=self.amountBox.value(),
            percentage=self.percentageBox.itemText(self.percentageBox.currentIndex())
        )
        if self.parent.CHOSEN_SERVICE:
            self.parent.CHOSEN_SERVICE.deleted = True
        self.parent.session.add(service)
        self.parent.session.commit()
        self.parent.populate_services()
        self.close()
        return

    def reject(self):
        self.close()
