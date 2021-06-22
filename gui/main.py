# import logging
import os
from datetime import date
from PySide2.QtCore import QDate, QTimer
from PySide2.QtWidgets import QMainWindow, QMessageBox
from sqlalchemy import extract
from sqlalchemy.sql.expression import desc
from database.models import (
    Bill,
    User,
    Contractor,
    Service,
    ServiceAssociation
)
from utils.converters import bill_name, bill_file_name, numtoword
from utils.file_handlers import save_to_json, save_from_json
from utils.pdf_creator import create_invoice_pdf
from .widgets.user import UserDialog
from .widgets.contractor import ContractorDialog
from .widgets.service import ServicesDialog
from .widgets.about import AboutDialog
from .widgets.calendar import CalendarDialog
from .widgets.licence import LicenceDialog
from .designer.main_window import Ui_MainWindow


class MainWindow(QMainWindow):

    DATE = QDate.currentDate().addDays(14)
    INVOICE_PREVIEW = None
    CHOSEN_CONTRACTOR = None
    CHOSEN_SERVICE = None

    def __init__(self, session):
        super().__init__()
        self.session = session
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.nd = None
        self.ui.listWidget.currentItemChanged.connect(self.self_contractor_changed)
        self.ui.listWidget_2.currentItemChanged.connect(self.service_item_changed)
        self.populate_contractors()
        self.populate_services()
        self.open_invoice_preview_file()
        timer = QTimer(self)
        timer.timeout.connect(self.monitor_state)
        timer.start(500)
        self.ui.calendarButton.setText(self.DATE.toString())
        self.ui.generateInvoice.clicked.connect(self.generate_invoice)
        self.ui.edit_my_info.triggered.connect(self.open_edit_user_dialog)
        self.ui.addContractor_2.triggered.connect(self.open_new_contractor_dialog)
        self.ui.editContractor.triggered.connect(self.edit_contractor)
        self.ui.delContractor.triggered.connect(self.delete_contractor)
        self.ui.editService.triggered.connect(self.edit_service)
        self.ui.delService.triggered.connect(self.delete_service)
        self.ui.calendarButton.clicked.connect(self.open_calendar_widget)
        self.ui.actionAbout.triggered.connect(self.open_about_widget)
        self.ui.addService.triggered.connect(self.open_new_service_dialog)
        self.ui.actionLicence.triggered.connect(self.open_licence_widget)
        self.ui.contractor_to_file.triggered.connect(self.export_contractors_to_file)
        self.ui.contractor_from_file.triggered.connect(self.import_contractors_from_file)
        self.show()

    def self_contractor_changed(self, curr):
        try:
            contractor_id = curr.data(1)
            contractor = self.session.query(Contractor).filter_by(id=contractor_id).first()
            self.CHOSEN_CONTRACTOR = contractor
            self.ui.editContractor.setEnabled(True)
            self.ui.delContractor.setEnabled(True)

        except AttributeError:
            # 'NoneType' object has no attribute 'data'
            pass

    def service_item_changed(self, curr):
        """ curr.data(1) zwraca id rekordu z bazy danych
        cyfra 1 to tylko numer roli jaką przypisałem do elementu listy
        """

        try:
            service_id = curr.data(1)
            service = self.session.query(Service).filter_by(id=service_id).first()
            self.CHOSEN_SERVICE = service
            self.ui.editService.setEnabled(True)
            self.ui.delService.setEnabled(True)
            self.ui.volumeBox.setEnabled(True)
            self.ui.measureBox.setEnabled(True)
            self.ui.amountBox.setEnabled(True)
            self.ui.amountBox.setValue(service.amount)

        except AttributeError:
            # 'NoneType' object has no attribute 'data'
            pass

    def populate_contractors(self):

        self.ui.listWidget.clear()
        contractors = (
            self.session.query(Contractor).filter_by(deleted=False).order_by(desc("id"))
        )
        for index, item in enumerate(contractors):
            self.ui.listWidget.addItem(item.__str__())
            contractor = self.ui.listWidget.item(index)
            contractor.setData(1, item.id)

    def populate_services(self):

        self.ui.listWidget_2.clear()
        services = (
            self.session.query(Service).filter_by(deleted=False).order_by(desc("id"))
        )
        for index, item in enumerate(services):
            self.ui.listWidget_2.addItem(item.name)
            service = self.ui.listWidget_2.item(index)
            service.setData(1, item.id)

    def open_invoice_preview_file(self):
        with open(os.path.join(os.getcwd(), "static", 'invoice_preview.html'), 'r', encoding='utf8') as file:
            self.INVOICE_PREVIEW = file.read()

    def monitor_state(self):
        if all([
            self.CHOSEN_SERVICE,
            self.CHOSEN_CONTRACTOR,
            self.session.query(User).order_by(desc("id")).first()
        ]):
            self.ui.generateInvoice.setEnabled(True)
            bills_count = (
                self.session.query(Bill).filter(
                    extract("month", Bill.created) == QDate.currentDate().month()
                )
            ).count()
            new_preview = self.INVOICE_PREVIEW.format(
                contractor=self.CHOSEN_CONTRACTOR,
                user=self.session.query(User).order_by(desc("id")).first(),
                service=self.CHOSEN_SERVICE,
                payment_date=self.DATE.toString('yyyy-MM-dd'),
                document_date=date.today().strftime('%Y-%m-%d'),
                invoice_name=bill_name(bills_count),
                selling_date=date.today().strftime('%B %Y'),
                partial_amount=self.ui.amountBox.value(),
                full_amount=self.ui.amountBox.value() * self.ui.volumeBox.value(),
                full_amount_to_word=numtoword(self.ui.amountBox.value() * self.ui.volumeBox.value()),
                volume=self.ui.volumeBox.value(),
            )
            self.ui.textBrowser.clear()
            self.ui.textBrowser.insertHtml(new_preview)
        else:
            self.ui.generateInvoice.setEnabled(False)

    def edit_contractor(self):

        self.nd = ContractorDialog(self, True)
        self.nd.show()

    def delete_contractor(self):

        contractor = self.CHOSEN_CONTRACTOR
        question = QMessageBox.question(
            self,
            "Usuwanie kontrahenta",
            f"Czy chcesz usunąć: {contractor}",
            QMessageBox.No | QMessageBox.Yes,
        )
        if question.name == b"Yes":
            contractor.deleted = True
            contractor.default = False
            self.session.commit()
        self.populate_contractors()

    def edit_service(self):
        self.nd = ServicesDialog(self, True)
        self.nd.show()

    def delete_service(self):
        service = self.CHOSEN_SERVICE
        question = QMessageBox.question(
            self,
            "Usuwanie usługi",
            f"Czy chcesz usunąć: {service}",
            QMessageBox.No | QMessageBox.Yes,
        )
        if question.name == b"Yes":
            service.deleted = True
            self.session.commit()
        self.populate_services()

    def generate_invoice(self):

        contractor = self.CHOSEN_CONTRACTOR
        service = self.CHOSEN_SERVICE
        user = self.session.query(User).order_by(desc("id")).first()
        bills_count = (
            self.session.query(Bill).filter(
                extract("month", Bill.created) == QDate.currentDate().month()
            )
        ).count()

        bill = Bill(
            user=user,
            contractor=contractor,
            payment_date=self.DATE.toPython(),
            name=bill_name(bills_count),
            amount=self.ui.amountBox.value() * self.ui.volumeBox.value()
        )
        assoc = ServiceAssociation(
            partial_amount=self.ui.amountBox.value(),
            full_amount=self.ui.amountBox.value() * self.ui.volumeBox.value(),
            volume=self.ui.volumeBox.value(),
        )
        assoc.service = service
        bill.services.append(assoc)
        self.session.add(bill)
        self.session.commit()
        bill = self.session.query(Bill).order_by(desc("id")).first()

        create_invoice_pdf(bill_file_name(bill_name(bills_count)), bill)

        QMessageBox.information(self, "Sukces", "Faktura została wygenerowana prawidłowo.")

    def open_edit_user_dialog(self):
        self.nd = UserDialog(self)
        self.nd.show()

    def open_new_contractor_dialog(self):
        self.nd = ContractorDialog(self, False)
        self.nd.show()

    def open_calendar_widget(self):
        self.nd = CalendarDialog(self)
        self.nd.show()

    def open_about_widget(self):
        self.nd = AboutDialog()
        self.nd.show()

    def open_new_service_dialog(self):
        self.nd = ServicesDialog(self, False)
        self.nd.show()

    def open_licence_widget(self):
        self.nd = LicenceDialog(self)
        self.nd.show()

    def export_contractors_to_file(self):
        contractors = (
            self.session.query(Contractor).filter_by(deleted=False).order_by(desc("id"))
        )
        save_to_json(self, contractors)

    def import_contractors_from_file(self):
        save_from_json(self, Contractor)
        self.populate_contractors()
