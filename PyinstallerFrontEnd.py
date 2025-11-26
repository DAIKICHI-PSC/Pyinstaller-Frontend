# -*- coding: utf-8 -*-
import sys
import os
from PySide6 import QtCore,QtGui,QtWidgets
from PIFE import Ui_MainWindow

selfDir = os.getcwd()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent) 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.checkBox1.clicked.connect(self.checkBox1_clicked)
        self.ui.checkBox2.clicked.connect(self.checkBox2_clicked)
        self.ui.checkBox3.clicked.connect(self.checkBox3_clicked)
        self.ui.checkBox4.clicked.connect(self.checkBox4_clicked)
        self.ui.pushButton1.clicked.connect(self.pushButton1_clicked)
        self.ui.pushButton2.clicked.connect(self.pushButton2_clicked)
        self.ui.pushButton3.clicked.connect(self.pushButton3_clicked)
        self.ui.pushButton4.clicked.connect(self.pushButton4_clicked)
        self.ui.pushButton5.clicked.connect(self.pushButton5_clicked)
        self.ui.pushButton6.clicked.connect(self.pushButton6_clicked)
        self.ui.pushButton7.clicked.connect(self.pushButton7_clicked)

        if os.path.isfile(selfDir + "/setting.txt") == True:
            text = ""
            f = open(selfDir + "/setting.txt", "r")
            text = f.readlines()
            f.close()
            self.ui.lineEdit1.setText(text[0].replace("\n", ""))
            self.ui.lineEdit2.setText(text[1].replace("\n", ""))
            self.ui.lineEdit3.setText(text[2].replace("\n", ""))
            if text[3].replace("\n", "") == "0":
                self.ui.checkBox1.setChecked(False)
            else:
                self.ui.checkBox1.setChecked(True)

            if text[4].replace("\n", "") == "0":
                self.ui.checkBox2.setChecked(False)
            else:
                self.ui.checkBox2.setChecked(True)

            if text[5].replace("\n", "") == "0":
                self.ui.checkBox3.setChecked(False)
            else:
                self.ui.checkBox3.setChecked(True)

            if text[6].replace("\n", "") == "0":
                self.ui.checkBox4.setChecked(False)
            else:
                self.ui.checkBox4.setChecked(True)

    def saveData(self):
        text = self.ui.lineEdit1.text() + "\n" + self.ui.lineEdit2.text() + "\n" + self.ui.lineEdit3.text() + "\n"
        if self.ui.checkBox1.isChecked() == False:
            text = text + "0\n"
        else:
            text = text + "1\n"
        if self.ui.checkBox2.isChecked() == False:
            text = text + "0\n"
        else:
            text = text + "1\n"
        if self.ui.checkBox3.isChecked() == False:
            text = text + "0\n"
        else:
            text = text + "1\n"
        if self.ui.checkBox4.isChecked() == False:
            text = text + "0\n"
        else:
            text = text + "1\n"
        f = open(selfDir + "/setting.txt", "w")
        f.writelines(text)
        f.close()

    def pushButton1_clicked(self):
        self.ui.lineEdit1.setText("")
        self.saveData()

    def pushButton2_clicked(self):
        FilePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Exe File", "",'exe File (*.exe)')
        if FilePath:
            self.ui.lineEdit1.setText(FilePath)
            self.saveData()

    def pushButton3_clicked(self):
        self.ui.lineEdit2.setText("")
        self.saveData()

    def pushButton4_clicked(self):
        if os.path.isfile(self.ui.lineEdit1.text()) == False:
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setWindowTitle("Message")
            msgbox.setText("Please set the path to Pyinstaller.")
            ret = msgbox.exec()
        elif os.path.isfile(self.ui.lineEdit2.text()) == False:
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setWindowTitle("Message")
            msgbox.setText("Please select a python file.")
            ret = msgbox.exec()
        elif self.ui.checkBox4.isChecked() == True and os.path.isfile(self.ui.lineEdit3.text()) == False:
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setWindowTitle("Message")
            msgbox.setText("Please select a icon file.")
            ret = msgbox.exec()
        else:
            piPath = self.ui.lineEdit1.text() + " "
            pyPath = self.ui.lineEdit2.text()

            if self.ui.checkBox1.isChecked() == False:
                op_onefile = ""
            else:
                op_onefile = " --onefile"

            if self.ui.checkBox2.isChecked() == False:
                op_clean = ""
            else:
                op_clean = " --clean"

            if self.ui.checkBox3.isChecked() == False:
                op_noconsole = ""
            else:
                op_noconsole = " --noconsole"

            if self.ui.checkBox4.isChecked() == False:
                op_icon = ""
            else:
                op_icon = " --icon=" + self.ui.lineEdit3.text()

            cmd = piPath + pyPath + op_onefile + op_clean + op_noconsole + op_icon

            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setWindowTitle("Message")
            msgbox.setText(cmd)
            ret = msgbox.exec()

            filename1 = pyPath.rsplit(".", 1)
            filename2 = filename1[0].rsplit("/", 1)
            os.chdir(filename2[0] + "/")

            ret = os.system(cmd)
            if ret == 0:
                msgbox = QtWidgets.QMessageBox(self)
                msgbox.setWindowTitle("Message")
                msgbox.setText("The selected file is converted.")
                ret = msgbox.exec()
            else: 
                msgbox = QtWidgets.QMessageBox(self)
                msgbox.setWindowTitle("Message")
                msgbox.setText("ERROR CODE : " + str(ret))
                ret = msgbox.exec()

    def pushButton5_clicked(self):
        FilePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Python File", "",'py File (*.py)')
        if FilePath:
            self.ui.lineEdit2.setText(FilePath)
            self.saveData()

    def pushButton6_clicked(self):
        self.ui.lineEdit3.setText("")
        self.saveData()

    def pushButton7_clicked(self):
        FilePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Icon File", "",'ico File (*.ico)')
        if FilePath:
            self.ui.lineEdit3.setText(FilePath)
            self.saveData()

    def checkBox1_clicked(self):
        self.saveData()

    def checkBox2_clicked(self):
        self.saveData()

    def checkBox3_clicked(self):
        self.saveData()

    def checkBox4_clicked(self):
        self.saveData()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dlg = MainWindow()
    dlg.show()
    sys.exit(app.exec())
