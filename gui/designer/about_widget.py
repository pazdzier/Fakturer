# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_widget.ui'
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
        Dialog.resize(584, 572)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 561, 551))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(539, 300))
        self.label_2.setPixmap(QPixmap(u"../../static/logo.png"))

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.tabWidget = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.formLayoutWidget = QWidget(self.tab_3)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 341, 114))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_4)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_6)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_8)

        self.label_9 = QLabel(self.formLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_9)

        self.label_10 = QLabel(self.formLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(0, QFormLayout.FieldRole, self.verticalSpacer)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayoutWidget_2 = QWidget(self.tab_4)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 531, 191))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.verticalLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.label_12)

        self.label_15 = QLabel(self.verticalLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.label_15)

        self.label_13 = QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.label_13)

        self.label_14 = QLabel(self.verticalLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.label_14)

        self.label_11 = QLabel(self.verticalLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.label_11)

        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.RichText)
        self.label.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.label)

        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"O tw\u00f3rcach", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Bartosz Puka", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Programista", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Pawe\u0142 Feliks", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Programista", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0141ukasz Pawlak", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Programista", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Piotr Waczak", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Programista", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"Sk\u0142ad developerski", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://pypi.org/project/Faker/\"><span style=\" text-decoration: underline; color:#0000ff;\">Faker</span></a></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://pypi.org/project/num2words/\"><span style=\" text-decoration: underline; color:#0000ff;\">num2words</span></a></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://pypi.org/project/PySide2/\"><span style=\" text-decoration: underline; color:#0000ff;\">PySide2</span></a></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://www.reportlab.com/dev/opensource/\"><span style=\" text-decoration: underline; color:#0000ff;\">ReportLab - Content to PDF Solutions</span></a></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://www.sqlalchemy.org/\"><span style=\" text-decoration: underline; color:#0000ff;\">SQLAlchemy - The Database Toolkit for Python</span></a></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://www.sphinx-doc.org/en/master/\"><span style=\" text-decoration: underline; color:#0000ff;\">SPHINX - Python Documentation Generator</span></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Dialog", u"Zewn\u0119trzne biblioteki", None))
    # retranslateUi

