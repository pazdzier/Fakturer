import os
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget
from gui.designer.about_widget import Ui_Dialog


class AboutDialog(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_2.setPixmap(QPixmap(os.path.join(os.getcwd(), "static", "logo.png")))
