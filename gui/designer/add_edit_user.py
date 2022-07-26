# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_edit_user.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(567, 358)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.first_name = QLineEdit(Dialog)
        self.first_name.setObjectName(u"first_name")

        self.gridLayout_2.addWidget(self.first_name, 0, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.last_name = QLineEdit(Dialog)
        self.last_name.setObjectName(u"last_name")

        self.gridLayout_2.addWidget(self.last_name, 1, 1, 1, 1)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.company_name = QLineEdit(Dialog)
        self.company_name.setObjectName(u"company_name")

        self.gridLayout_2.addWidget(self.company_name, 2, 1, 1, 1)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)

        self.nip = QLineEdit(Dialog)
        self.nip.setObjectName(u"nip")

        self.gridLayout_2.addWidget(self.nip, 3, 1, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)

        self.street = QLineEdit(Dialog)
        self.street.setObjectName(u"street")

        self.gridLayout_2.addWidget(self.street, 4, 1, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)

        self.city = QLineEdit(Dialog)
        self.city.setObjectName(u"city")

        self.gridLayout_2.addWidget(self.city, 5, 1, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 1)

        self.zip_code = QLineEdit(Dialog)
        self.zip_code.setObjectName(u"zip_code")

        self.gridLayout_2.addWidget(self.zip_code, 6, 1, 1, 1)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 7, 0, 1, 1)

        self.account_number = QLineEdit(Dialog)
        self.account_number.setObjectName(u"account_number")

        self.gridLayout_2.addWidget(self.account_number, 7, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 8, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)


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

