# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PIFE.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1051, 291)
        MainWindow.setMinimumSize(QSize(1051, 291))
        MainWindow.setMaximumSize(QSize(1051, 291))
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox1 = QGroupBox(self.centralwidget)
        self.groupBox1.setObjectName(u"groupBox1")
        self.groupBox1.setGeometry(QRect(10, 10, 1031, 61))
        self.lineEdit1 = QLineEdit(self.groupBox1)
        self.lineEdit1.setObjectName(u"lineEdit1")
        self.lineEdit1.setGeometry(QRect(10, 20, 811, 31))
        self.pushButton2 = QPushButton(self.groupBox1)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setGeometry(QRect(930, 20, 93, 31))
        self.pushButton1 = QPushButton(self.groupBox1)
        self.pushButton1.setObjectName(u"pushButton1")
        self.pushButton1.setGeometry(QRect(830, 20, 93, 31))
        self.groupBox2 = QGroupBox(self.centralwidget)
        self.groupBox2.setObjectName(u"groupBox2")
        self.groupBox2.setGeometry(QRect(10, 80, 1031, 61))
        self.lineEdit2 = QLineEdit(self.groupBox2)
        self.lineEdit2.setObjectName(u"lineEdit2")
        self.lineEdit2.setGeometry(QRect(10, 20, 711, 31))
        self.pushButton5 = QPushButton(self.groupBox2)
        self.pushButton5.setObjectName(u"pushButton5")
        self.pushButton5.setGeometry(QRect(930, 20, 93, 31))
        self.pushButton4 = QPushButton(self.groupBox2)
        self.pushButton4.setObjectName(u"pushButton4")
        self.pushButton4.setGeometry(QRect(830, 20, 93, 31))
        self.pushButton3 = QPushButton(self.groupBox2)
        self.pushButton3.setObjectName(u"pushButton3")
        self.pushButton3.setGeometry(QRect(730, 20, 93, 31))
        self.groupBox4 = QGroupBox(self.centralwidget)
        self.groupBox4.setObjectName(u"groupBox4")
        self.groupBox4.setGeometry(QRect(10, 220, 151, 61))
        self.checkBox1 = QCheckBox(self.groupBox4)
        self.checkBox1.setObjectName(u"checkBox1")
        self.checkBox1.setGeometry(QRect(10, 20, 61, 16))
        self.checkBox1.setChecked(True)
        self.checkBox2 = QCheckBox(self.groupBox4)
        self.checkBox2.setObjectName(u"checkBox2")
        self.checkBox2.setGeometry(QRect(10, 40, 61, 16))
        self.checkBox2.setChecked(True)
        self.checkBox3 = QCheckBox(self.groupBox4)
        self.checkBox3.setObjectName(u"checkBox3")
        self.checkBox3.setGeometry(QRect(70, 20, 71, 16))
        self.checkBox3.setChecked(True)
        self.checkBox4 = QCheckBox(self.groupBox4)
        self.checkBox4.setObjectName(u"checkBox4")
        self.checkBox4.setGeometry(QRect(70, 40, 71, 16))
        self.checkBox4.setChecked(False)
        self.groupBox3 = QGroupBox(self.centralwidget)
        self.groupBox3.setObjectName(u"groupBox3")
        self.groupBox3.setGeometry(QRect(10, 150, 1031, 61))
        self.lineEdit3 = QLineEdit(self.groupBox3)
        self.lineEdit3.setObjectName(u"lineEdit3")
        self.lineEdit3.setGeometry(QRect(10, 20, 811, 31))
        self.pushButton7 = QPushButton(self.groupBox3)
        self.pushButton7.setObjectName(u"pushButton7")
        self.pushButton7.setGeometry(QRect(930, 20, 93, 31))
        self.pushButton6 = QPushButton(self.groupBox3)
        self.pushButton6.setObjectName(u"pushButton6")
        self.pushButton6.setGeometry(QRect(830, 20, 93, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pyinstaller Front End", None))
        self.groupBox1.setTitle(QCoreApplication.translate("MainWindow", u"LOCATION OF pyinstaller.exe", None))
        self.pushButton2.setText(QCoreApplication.translate("MainWindow", u"OPEN", None))
        self.pushButton1.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.groupBox2.setTitle(QCoreApplication.translate("MainWindow", u"LOCATION OF PYTHON FILE", None))
        self.pushButton5.setText(QCoreApplication.translate("MainWindow", u"OPEN", None))
        self.pushButton4.setText(QCoreApplication.translate("MainWindow", u"EXEC", None))
        self.pushButton3.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.groupBox4.setTitle(QCoreApplication.translate("MainWindow", u"OPTION", None))
        self.checkBox1.setText(QCoreApplication.translate("MainWindow", u"onefile", None))
        self.checkBox2.setText(QCoreApplication.translate("MainWindow", u"clean", None))
        self.checkBox3.setText(QCoreApplication.translate("MainWindow", u"noconsole", None))
        self.checkBox4.setText(QCoreApplication.translate("MainWindow", u"icon", None))
        self.groupBox3.setTitle(QCoreApplication.translate("MainWindow", u"LOCATION OF ICON FILE", None))
        self.pushButton7.setText(QCoreApplication.translate("MainWindow", u"OPEN", None))
        self.pushButton6.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
    # retranslateUi

