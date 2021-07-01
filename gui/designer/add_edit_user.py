# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_edit_user.ui'
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
        Dialog.resize(567, 358)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.first_name = QLineEdit(Dialog)
        self.first_name.setObjectName(u"first_name")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.first_name)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.last_name = QLineEdit(Dialog)
        self.last_name.setObjectName(u"last_name")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.last_name)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.company_name = QLineEdit(Dialog)
        self.company_name.setObjectName(u"company_name")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.company_name)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.nip = QLineEdit(Dialog)
        self.nip.setObjectName(u"nip")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.nip)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.street = QLineEdit(Dialog)
        self.street.setObjectName(u"street")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.street)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.city = QLineEdit(Dialog)
        self.city.setObjectName(u"city")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.city)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_5)

        self.zip_code = QLineEdit(Dialog)
        self.zip_code.setObjectName(u"zip_code")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.zip_code)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_6)

        self.account_number = QLineEdit(Dialog)
        self.account_number.setObjectName(u"account_number")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.account_number)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.buttonBox)


        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Edycja danych u\u017cytkownika", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Imi\u0119", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nazwisko", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Nazwa", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"NIP", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Ulica", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Miasto", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Kod pocztowy", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Numer rachunku", None))
        self.account_number.setPlaceholderText("")
    # retranslateUi

