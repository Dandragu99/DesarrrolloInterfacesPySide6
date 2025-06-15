# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Clase1UI.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(782, 682)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 70, 61, 31))
        self.btnIncrementar = QPushButton(self.centralwidget)
        self.btnIncrementar.setObjectName(u"btnIncrementar")
        self.btnIncrementar.setGeometry(QRect(100, 120, 75, 24))
        self.btnDecrementar = QPushButton(self.centralwidget)
        self.btnDecrementar.setObjectName(u"btnDecrementar")
        self.btnDecrementar.setGeometry(QRect(230, 120, 75, 24))
        self.resetear = QPushButton(self.centralwidget)
        self.resetear.setObjectName(u"resetear")
        self.resetear.setGeometry(QRect(360, 120, 75, 24))
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(130, 180, 291, 64))
        self.sumar = QPushButton(self.centralwidget)
        self.sumar.setObjectName(u"sumar")
        self.sumar.setGeometry(QRect(160, 300, 75, 24))
        self.restar = QPushButton(self.centralwidget)
        self.restar.setObjectName(u"restar")
        self.restar.setGeometry(QRect(270, 300, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 782, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnIncrementar.setText(QCoreApplication.translate("MainWindow", u" BTNIncrementar", None))
        self.btnDecrementar.setText(QCoreApplication.translate("MainWindow", u"BTNDecrementar", None))
        self.resetear.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.sumar.setText(QCoreApplication.translate("MainWindow", u"sumar", None))
        self.restar.setText(QCoreApplication.translate("MainWindow", u"restar", None))
    # retranslateUi

