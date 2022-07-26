from PySide6.QtGui import Qt
from PySide6.QtWidgets import (
    QWidget,
    QTableView,
    QTableWidgetItem,
    QHeaderView
)
from gui.designer.invoices import Ui_Dialog
from database.models import Bill
from utils.pdf_creator import create_invoice_pdf


class InvoicesDialog(QWidget, Ui_Dialog):

    SELECTED_INVOICE = None

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
        self.populate_invoices()
        self.tableWidget.clicked.connect(self.select_invoice)
        self.pushButton.clicked.connect(self.create_invoice)

    def populate_invoices(self):
        bills = self.parent.session.query(Bill).filter_by(deleted=False)
        self.tableWidget.setRowCount(bills.count())
        self.tableWidget.setSelectionBehavior(QTableView.SelectRows)
        table = self.tableWidget.horizontalHeader()
        table.setSectionResizeMode(0, QHeaderView.Stretch)
        for index, invoice in enumerate(bills):
            download_item = QTableWidgetItem(invoice.name)
            download_item.setData(200, invoice)
            download_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            download_item.setText(invoice.name)
            self.tableWidget.setItem(index, 0, download_item)

    def select_invoice(self, clickedIndex):
        if self.SELECTED_INVOICE == clickedIndex.model().data(clickedIndex, 200):
            self.pushButton.setEnabled(False)
            self.SELECTED_INVOICE = None
            self.tableWidget.clearSelection()
        else:
            self.SELECTED_INVOICE = clickedIndex.model().data(clickedIndex, 200)
            self.pushButton.setEnabled(True)

    def create_invoice(self):
        create_invoice_pdf(str(), self.SELECTED_INVOICE)
