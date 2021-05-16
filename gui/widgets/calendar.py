from datetime import date
from PySide2.QtWidgets import QWidget
from gui.designer.calendar_widget import Ui_Dialog


class CalendarDialog(QWidget, Ui_Dialog):

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
        self.calendarWidget.setMinimumDate(date.today())
        self.pushButton.clicked.connect(self.get_date)

    def get_date(self):
        self.parent.DATE = self.calendarWidget.selectedDate()
        self.parent.ui.calendarButton.setText(self.parent.DATE.toString())
        self.close()
