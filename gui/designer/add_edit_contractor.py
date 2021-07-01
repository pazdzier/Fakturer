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
        Dialog.resize(695, 279)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.company_name = QLineEdit(Dialog)
        self.company_name.setObjectName(u"company_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.company_name)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.nip = QLineEdit(Dialog)
        self.nip.setObjectName(u"nip")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.nip)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.street = QLineEdit(Dialog)
        self.street.setObjectName(u"street")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.street)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.city = QLineEdit(Dialog)
        self.city.setObjectName(u"city")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.city)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.zip_code = QLineEdit(Dialog)
        self.zip_code.setObjectName(u"zip_code")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.zip_code)

        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.checkBox)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.buttonBox)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)


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

