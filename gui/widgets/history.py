import json
import os
from PySide2.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from gui.designer.history import Ui_Dialog
from utils.constants import STATIC


class HistoryDialog(QWidget, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.history_lst = None
        self.setupUi(self)
        self.open_file_with_history()
        self.populate_history()

    def open_file_with_history(self):
        with open(os.path.join(STATIC, 'history.json'), 'r') as file:
            self.history_lst = json.loads(file.read())

    def populate_history(self):
        self.tableWidget.setRowCount(len(self.history_lst))
        table = self.tableWidget.horizontalHeader()
        table.setSectionResizeMode(0, QHeaderView.Stretch)
        for i in range(len(self.history_lst)):
            created_date = self.history_lst[i][0]
            item = QTableWidgetItem(str(self.history_lst[i][1]))
            item.setToolTip(f'Dodano w dniu {created_date}')
            self.tableWidget.setItem(i, 0, item)
