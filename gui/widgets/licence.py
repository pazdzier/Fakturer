import os
from PySide2.QtWidgets import QWidget
from gui.designer.licence_widget import Ui_Dialog


class LicenceDialog(QWidget, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
        self.populate_licence()

    def populate_licence(self):
        with open(os.path.join(os.getcwd(), "LICENSE"), "r") as file:
            text = file.read()
            self.textBrowser.setText(text)
