# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1095, 640)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.addContractor = QAction(MainWindow)
        self.addContractor.setObjectName(u"addContractor")
        self.addContractor_2 = QAction(MainWindow)
        self.addContractor_2.setObjectName(u"addContractor_2")
        self.addContractor_2.setEnabled(True)
        self.edit_my_info = QAction(MainWindow)
        self.edit_my_info.setObjectName(u"edit_my_info")
        self.actionHistory = QAction(MainWindow)
        self.actionHistory.setObjectName(u"actionHistory")
        self.actionHistory.setCheckable(False)
        self.actionHistory.setEnabled(True)
        self.editContractor = QAction(MainWindow)
        self.editContractor.setObjectName(u"editContractor")
        self.editContractor.setEnabled(False)
        self.delContractor = QAction(MainWindow)
        self.delContractor.setObjectName(u"delContractor")
        self.delContractor.setEnabled(False)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.addService = QAction(MainWindow)
        self.addService.setObjectName(u"addService")
        self.editService = QAction(MainWindow)
        self.editService.setObjectName(u"editService")
        self.editService.setEnabled(False)
        self.delService = QAction(MainWindow)
        self.delService.setObjectName(u"delService")
        self.delService.setEnabled(False)
        self.actionLicence = QAction(MainWindow)
        self.actionLicence.setObjectName(u"actionLicence")
        self.actionInstrukcja_obs_ugi = QAction(MainWindow)
        self.actionInstrukcja_obs_ugi.setObjectName(u"actionInstrukcja_obs_ugi")
        self.actionInstrukcja_obs_ugi.setEnabled(False)
        self.contractor_to_file = QAction(MainWindow)
        self.contractor_to_file.setObjectName(u"contractor_to_file")
        self.contractor_from_file = QAction(MainWindow)
        self.contractor_from_file.setObjectName(u"contractor_from_file")
        self.user_to_file = QAction(MainWindow)
        self.user_to_file.setObjectName(u"user_to_file")
        self.user_to_file.setEnabled(False)
        self.user_from_file = QAction(MainWindow)
        self.user_from_file.setObjectName(u"user_from_file")
        self.user_from_file.setEnabled(False)
        self.menu_invoices = QAction(MainWindow)
        self.menu_invoices.setObjectName(u"menu_invoices")
        self.actionEvidence = QAction(MainWindow)
        self.actionEvidence.setObjectName(u"actionEvidence")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(0, 0))
        self.listWidget.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.listWidget)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.listWidget_2 = QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.listWidget_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.amountBox = QDoubleSpinBox(self.centralwidget)
        self.amountBox.setObjectName(u"amountBox")
        self.amountBox.setEnabled(False)
        self.amountBox.setReadOnly(False)
        self.amountBox.setMinimum(1.000000000000000)
        self.amountBox.setMaximum(99999.990000000005239)

        self.gridLayout.addWidget(self.amountBox, 3, 2, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 3, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)

        self.volumeBox = QSpinBox(self.centralwidget)
        self.volumeBox.setObjectName(u"volumeBox")
        self.volumeBox.setEnabled(False)
        self.volumeBox.setMinimum(1)
        self.volumeBox.setMaximum(99)

        self.gridLayout.addWidget(self.volumeBox, 3, 0, 1, 1)

        self.measureBox = QComboBox(self.centralwidget)
        self.measureBox.addItem("")
        self.measureBox.setObjectName(u"measureBox")

        self.gridLayout.addWidget(self.measureBox, 3, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.calendarButton = QPushButton(self.centralwidget)
        self.calendarButton.setObjectName(u"calendarButton")

        self.gridLayout.addWidget(self.calendarButton, 2, 4, 1, 1)

        self.generateInvoice = QPushButton(self.centralwidget)
        self.generateInvoice.setObjectName(u"generateInvoice")
        self.generateInvoice.setEnabled(False)

        self.gridLayout.addWidget(self.generateInvoice, 3, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy1)
        self.textBrowser.setMinimumSize(QSize(490, 0))
        self.textBrowser.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.textBrowser.setFrameShape(QFrame.StyledPanel)
        self.textBrowser.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.textBrowser)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1095, 21))
        self.menuKontrahenci = QMenu(self.menuBar)
        self.menuKontrahenci.setObjectName(u"menuKontrahenci")
        self.menuOMnie = QMenu(self.menuBar)
        self.menuOMnie.setObjectName(u"menuOMnie")
        self.invoices = QMenu(self.menuBar)
        self.invoices.setObjectName(u"invoices")
        self.invoices.setEnabled(True)
        self.invoices.setTearOffEnabled(False)
        self.menuO_programie = QMenu(self.menuBar)
        self.menuO_programie.setObjectName(u"menuO_programie")
        self.menuO_programie.setLayoutDirection(Qt.LeftToRight)
        self.menuUs_ugi = QMenu(self.menuBar)
        self.menuUs_ugi.setObjectName(u"menuUs_ugi")
        self.menuEwidencja_przychod_w = QMenu(self.menuBar)
        self.menuEwidencja_przychod_w.setObjectName(u"menuEwidencja_przychod_w")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuOMnie.menuAction())
        self.menuBar.addAction(self.menuKontrahenci.menuAction())
        self.menuBar.addAction(self.menuUs_ugi.menuAction())
        self.menuBar.addAction(self.invoices.menuAction())
        self.menuBar.addAction(self.menuEwidencja_przychod_w.menuAction())
        self.menuBar.addAction(self.menuO_programie.menuAction())
        self.menuKontrahenci.addAction(self.addContractor_2)
        self.menuKontrahenci.addAction(self.editContractor)
        self.menuKontrahenci.addAction(self.delContractor)
        self.menuKontrahenci.addAction(self.contractor_to_file)
        self.menuKontrahenci.addAction(self.contractor_from_file)
        self.menuOMnie.addAction(self.edit_my_info)
        self.menuOMnie.addAction(self.user_to_file)
        self.menuOMnie.addAction(self.user_from_file)
        self.invoices.addAction(self.menu_invoices)
        self.menuO_programie.addAction(self.actionHistory)
        self.menuO_programie.addAction(self.actionAbout)
        self.menuO_programie.addAction(self.actionLicence)
        self.menuO_programie.addAction(self.actionInstrukcja_obs_ugi)
        self.menuUs_ugi.addAction(self.addService)
        self.menuUs_ugi.addAction(self.editService)
        self.menuUs_ugi.addAction(self.delService)
        self.menuEwidencja_przychod_w.addAction(self.actionEvidence)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fakturer 2.0", None))
        self.addContractor.setText(QCoreApplication.translate("MainWindow", u"Dodaj", None))
        self.addContractor_2.setText(QCoreApplication.translate("MainWindow", u"Dodaj", None))
        self.edit_my_info.setText(QCoreApplication.translate("MainWindow", u"Edycja", None))
        self.actionHistory.setText(QCoreApplication.translate("MainWindow", u"Historia zmian", None))
        self.editContractor.setText(QCoreApplication.translate("MainWindow", u"Edytuj zaznaczonego", None))
        self.delContractor.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144 zaznaczonego", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"O tw\u00f3rcach", None))
        self.addService.setText(QCoreApplication.translate("MainWindow", u"Dodaj", None))
        self.editService.setText(QCoreApplication.translate("MainWindow", u"Edytuj", None))
        self.delService.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144", None))
        self.actionLicence.setText(QCoreApplication.translate("MainWindow", u"Licencja", None))
        self.actionInstrukcja_obs_ugi.setText(QCoreApplication.translate("MainWindow", u"Instrukcja obs\u0142ugi", None))
        self.contractor_to_file.setText(QCoreApplication.translate("MainWindow", u"Eksport do pliku", None))
        self.contractor_from_file.setText(QCoreApplication.translate("MainWindow", u"Import z pliku", None))
        self.user_to_file.setText(QCoreApplication.translate("MainWindow", u"Eksport do pliku", None))
        self.user_from_file.setText(QCoreApplication.translate("MainWindow", u"Import z pliku", None))
        self.menu_invoices.setText(QCoreApplication.translate("MainWindow", u"Wy\u015bwietl", None))
        self.actionEvidence.setText(QCoreApplication.translate("MainWindow", u"Ewidencja przychod\u00f3w", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Wybierz kontrahenta", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Wybierz us\u0142ug\u0119", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Termin p\u0142atno\u015bci", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Cena jednostkowa [z\u0142, gr]", None))
        self.measureBox.setItemText(0, QCoreApplication.translate("MainWindow", u"szt.", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"j.m.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107", None))
        self.calendarButton.setText(QCoreApplication.translate("MainWindow", u"wybierz ...", None))
        self.generateInvoice.setText(QCoreApplication.translate("MainWindow", u"Generuj faktur\u0119", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Witaj w aplikacji Fakturer - wygodnym narz\u0119dziu do automatyzacji wystawiania rachunk\u00f3w dla os\u00f3b b\u0119d\u0105cych na umowach b2b. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Przed wystawieniem pierwszej fa"
                        "ktury:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">uzupe\u0142nij swoje dane w zak\u0142adce <span style=\" color:#0000ff;\">Moje dane</span> </li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">dodaj kontrahenta w zak\u0142ace <span style=\" color:#0000ff;\">Kontrahenci</span> </li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Wska\u017c rodzaj i ilo\u015b\u0107 wykonany us\u0142ug w zak\u0142adce <span style=\" color:#0000ff;\">Us\u0142ugi</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-ind"
                        "ent:0; text-indent:0px;\">Wska\u017c termin p\u0142atno\u015bci w pozycji <span style=\" color:#0000ff;\">Termin p\u0142atno\u015bc</span>i (domy\u015blnie ustawione jest 14 dni kalendarzowych)</li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -"
                        "qt-block-indent:1; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Dzi\u0119kujemy za wyb\u00f3r aplikacji Fakturer<br /><br />zesp\u00f3\u0142 developerski.</span></p></body></html>", None))
        self.menuKontrahenci.setTitle(QCoreApplication.translate("MainWindow", u"Kontrahenci", None))
        self.menuOMnie.setTitle(QCoreApplication.translate("MainWindow", u"Moje dane", None))
        self.invoices.setTitle(QCoreApplication.translate("MainWindow", u"Historia Faktur", None))
        self.menuO_programie.setTitle(QCoreApplication.translate("MainWindow", u"O programie", None))
        self.menuUs_ugi.setTitle(QCoreApplication.translate("MainWindow", u"Us\u0142ugi", None))
        self.menuEwidencja_przychod_w.setTitle(QCoreApplication.translate("MainWindow", u"Narz\u0119dzia", None))
    # retranslateUi

