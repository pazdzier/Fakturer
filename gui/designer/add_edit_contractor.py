# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_edit_contractor.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(695, 279)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.company_name = QLineEdit(Dialog)
        self.company_name.setObjectName(u"company_name")

        self.gridLayout_2.addWidget(self.company_name, 0, 1, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.nip = QLineEdit(Dialog)
        self.nip.setObjectName(u"nip")

        self.gridLayout_2.addWidget(self.nip, 1, 1, 1, 1)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.street = QLineEdit(Dialog)
        self.street.setObjectName(u"street")

        self.gridLayout_2.addWidget(self.street, 2, 1, 1, 1)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)

        self.city = QLineEdit(Dialog)
        self.city.setObjectName(u"city")

        self.gridLayout_2.addWidget(self.city, 3, 1, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)

        self.zip_code = QLineEdit(Dialog)
        self.zip_code.setObjectName(u"zip_code")

        self.gridLayout_2.addWidget(self.zip_code, 4, 1, 1, 1)

        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox, 5, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 6, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)


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

