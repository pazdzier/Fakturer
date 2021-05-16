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
        MainWindow.resize(1458, 804)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
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
        self.actionHistoria_zmian = QAction(MainWindow)
        self.actionHistoria_zmian.setObjectName(u"actionHistoria_zmian")
        self.actionHistoria_zmian.setCheckable(False)
        self.actionHistoria_zmian.setEnabled(False)
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 1431, 711))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 151, 16))
        self.formLayoutWidget = QWidget(self.groupBox_2)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(250, 611, 451, 91))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.calendarButton = QPushButton(self.formLayoutWidget)
        self.calendarButton.setObjectName(u"calendarButton")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.calendarButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(1, QFormLayout.FieldRole, self.verticalSpacer)

        self.generateInvoice = QPushButton(self.formLayoutWidget)
        self.generateInvoice.setObjectName(u"generateInvoice")
        self.generateInvoice.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.generateInvoice)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 300, 121, 19))
        self.listWidget_2 = QListWidget(self.groupBox_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(10, 320, 691, 211))
        self.listWidget_2.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget = QWidget(self.groupBox_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 540, 343, 61))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)

        self.amountBox = QDoubleSpinBox(self.gridLayoutWidget)
        self.amountBox.setObjectName(u"amountBox")
        self.amountBox.setEnabled(False)
        self.amountBox.setReadOnly(False)
        self.amountBox.setMinimum(1.000000000000000)
        self.amountBox.setMaximum(99999.990000000005239)

        self.gridLayout.addWidget(self.amountBox, 3, 2, 1, 1)

        self.volumeBox = QSpinBox(self.gridLayoutWidget)
        self.volumeBox.setObjectName(u"volumeBox")
        self.volumeBox.setEnabled(False)
        self.volumeBox.setMinimum(1)
        self.volumeBox.setMaximum(99)

        self.gridLayout.addWidget(self.volumeBox, 3, 0, 1, 1)

        self.measureBox = QComboBox(self.gridLayoutWidget)
        self.measureBox.addItem("")
        self.measureBox.setObjectName(u"measureBox")

        self.gridLayout.addWidget(self.measureBox, 3, 1, 1, 1)

        self.listWidget = QListWidget(self.groupBox_2)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 50, 691, 211))
        self.listWidget.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.textBrowser = QTextBrowser(self.groupBox_3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QRect(120, 30, 501, 671))
        self.textBrowser.setMinimumSize(QSize(501, 0))
        self.textBrowser.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.textBrowser.setFrameShape(QFrame.StyledPanel)
        self.textBrowser.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.groupBox_3)

        self.groupBox_3.raise_()
        self.groupBox_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1458, 31))
        self.menuKontrahenci = QMenu(self.menuBar)
        self.menuKontrahenci.setObjectName(u"menuKontrahenci")
        self.menuOMnie = QMenu(self.menuBar)
        self.menuOMnie.setObjectName(u"menuOMnie")
        self.menuHistoria_Faktur = QMenu(self.menuBar)
        self.menuHistoria_Faktur.setObjectName(u"menuHistoria_Faktur")
        self.menuHistoria_Faktur.setEnabled(False)
        self.menuO_programie = QMenu(self.menuBar)
        self.menuO_programie.setObjectName(u"menuO_programie")
        self.menuO_programie.setLayoutDirection(Qt.LeftToRight)
        self.menuUs_ugi = QMenu(self.menuBar)
        self.menuUs_ugi.setObjectName(u"menuUs_ugi")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuOMnie.menuAction())
        self.menuBar.addAction(self.menuKontrahenci.menuAction())
        self.menuBar.addAction(self.menuUs_ugi.menuAction())
        self.menuBar.addAction(self.menuHistoria_Faktur.menuAction())
        self.menuBar.addAction(self.menuO_programie.menuAction())
        self.menuKontrahenci.addAction(self.addContractor_2)
        self.menuKontrahenci.addAction(self.editContractor)
        self.menuKontrahenci.addAction(self.delContractor)
        self.menuOMnie.addAction(self.edit_my_info)
        self.menuO_programie.addAction(self.actionHistoria_zmian)
        self.menuO_programie.addAction(self.actionAbout)
        self.menuO_programie.addAction(self.actionLicence)
        self.menuO_programie.addAction(self.actionInstrukcja_obs_ugi)
        self.menuUs_ugi.addAction(self.addService)
        self.menuUs_ugi.addAction(self.editService)
        self.menuUs_ugi.addAction(self.delService)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fakturer 2.0", None))
        self.addContractor.setText(QCoreApplication.translate("MainWindow", u"Dodaj", None))
        self.addContractor_2.setText(QCoreApplication.translate("MainWindow", u"Dodaj", None))
        self.edit_my_info.setText(QCoreApplication.translate("MainWindow", u"Edycja", None))
        self.actionHistoria_zmian.setText(QCoreApplication.translate("MainWindow", u"Historia zmian", None))
        self.editContractor.setText(QCoreApplication.translate("MainWindow", u"Edytuj zaznaczonego", None))
        self.delContractor.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144 zaznaczonego", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"O tw\u00f3rcach", None))
        self.addService.setText(QCoreApplication.translate("MainWindow", u"Dodaj", None))
        self.editService.setText(QCoreApplication.translate("MainWindow", u"Edytuj", None))
        self.delService.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144", None))
        self.actionLicence.setText(QCoreApplication.translate("MainWindow", u"Licencja", None))
        self.actionInstrukcja_obs_ugi.setText(QCoreApplication.translate("MainWindow", u"Instrukcja obs\u0142ugi", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Wystaw faktur\u0119", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Wybierz kontrahenta", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Termin p\u0142atno\u015bci", None))
        self.calendarButton.setText(QCoreApplication.translate("MainWindow", u"wybierz ...", None))
        self.generateInvoice.setText(QCoreApplication.translate("MainWindow", u"Generuj faktur\u0119", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Wybierz us\u0142ug\u0119", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"j.m.", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Cena jednostkowa [z\u0142, gr]", None))
        self.measureBox.setItemText(0, QCoreApplication.translate("MainWindow", u"szt.", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Skr\u00f3cona instrukcja", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Witaj w aplikacji Fakturer - wygodnym narz\u0119dziu do automatyzacji wystawiania rachunk\u00f3w dla os\u00f3b b\u0119d\u0105cych na umowach b2b. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Przed wystawieniem pierwszej faktury:</p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-"
                        "right: 0px; -qt-list-indent: 1;\"><li style=\"\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">uzupe\u0142nij swoje dane w zak\u0142adce <span style=\" color:#0000ff;\">Moje dane</span> </li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">dodaj kontrahenta w zak\u0142ace <span style=\" color:#0000ff;\">Kontrahenci</span> </li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Wska\u017c rodzaj i ilo\u015b\u0107 wykonany us\u0142ug w zak\u0142adce <span style=\" color:#0000ff;\">Us\u0142ugi</span></li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Wska\u017c termin p\u0142atno\u015bci w pozycji <span style=\" color:#0000ff;\">Termin p\u0142atno\u015bc</span>i (domy\u015blnie "
                        "ustawione jest 14 dni kalendarzowych)</li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><br /></p>\n"
"<"
                        "p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dzi\u0119kujemy za wyb\u00f3r aplikacji Fakturer<br /><br />zesp\u00f3\u0142 developerski.</p></body></html>", None))
        self.menuKontrahenci.setTitle(QCoreApplication.translate("MainWindow", u"Kontrahenci", None))
        self.menuOMnie.setTitle(QCoreApplication.translate("MainWindow", u"Moje dane", None))
        self.menuHistoria_Faktur.setTitle(QCoreApplication.translate("MainWindow", u"Historia Faktur", None))
        self.menuO_programie.setTitle(QCoreApplication.translate("MainWindow", u"O programie", None))
        self.menuUs_ugi.setTitle(QCoreApplication.translate("MainWindow", u"Us\u0142ugi", None))
    # retranslateUi

