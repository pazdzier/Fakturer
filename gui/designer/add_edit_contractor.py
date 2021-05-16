# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_edit_contractor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(503, 306)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 481, 191))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.company_name = QLineEdit(self.formLayoutWidget)
        self.company_name.setObjectName(u"company_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.company_name)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.nip = QLineEdit(self.formLayoutWidget)
        self.nip.setObjectName(u"nip")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.nip)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.street = QLineEdit(self.formLayoutWidget)
        self.street.setObjectName(u"street")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.street)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.city = QLineEdit(self.formLayoutWidget)
        self.city.setObjectName(u"city")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.city)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.zip_code = QLineEdit(self.formLayoutWidget)
        self.zip_code.setObjectName(u"zip_code")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.zip_code)

        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 200, 481, 97))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Nazwa", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"NIP", None))
        self.nip.setInputMask("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Ulica", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Miasto", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Kod pocztowy", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Domy\u015blny kontrahent", None))
    # retranslateUi

