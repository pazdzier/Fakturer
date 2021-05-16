# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'services.ui'
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
        Dialog.resize(533, 481)
        self.gridLayoutWidget_2 = QWidget(Dialog)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 511, 461))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.serviceEdit = QPlainTextEdit(self.gridLayoutWidget_2)
        self.serviceEdit.setObjectName(u"serviceEdit")

        self.verticalLayout.addWidget(self.serviceEdit)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(7)
        self.label_6.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.char_limit = QLabel(self.gridLayoutWidget_2)
        self.char_limit.setObjectName(u"char_limit")
        self.char_limit.setFont(font)

        self.horizontalLayout_3.addWidget(self.char_limit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.volumeBox = QSpinBox(self.gridLayoutWidget_2)
        self.volumeBox.setObjectName(u"volumeBox")
        self.volumeBox.setEnabled(False)
        self.volumeBox.setMinimum(1)
        self.volumeBox.setMaximum(1)

        self.gridLayout.addWidget(self.volumeBox, 3, 0, 1, 1)

        self.amountBox = QDoubleSpinBox(self.gridLayoutWidget_2)
        self.amountBox.setObjectName(u"amountBox")
        self.amountBox.setMinimum(1.000000000000000)
        self.amountBox.setMaximum(99999.990000000005239)

        self.gridLayout.addWidget(self.amountBox, 3, 3, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(self.gridLayoutWidget_2)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 5, 3, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 4, 3, 1, 1)

        self.measureBox = QComboBox(self.gridLayoutWidget_2)
        self.measureBox.addItem("")
        self.measureBox.setObjectName(u"measureBox")

        self.gridLayout.addWidget(self.measureBox, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nazwa us\u0142ugi", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"znak\u00f3w:", None))
        self.char_limit.setText(QCoreApplication.translate("Dialog", u"160", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"j.m.", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Ilo\u015b\u0107", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Cena jednostkowa [z\u0142, gr]", None))
        self.measureBox.setItemText(0, QCoreApplication.translate("Dialog", u"szt.", None))

    # retranslateUi

