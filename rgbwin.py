# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Documents/rgbwin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.redBut = QtWidgets.QRadioButton(Dialog)
        self.redBut.setGeometry(QtCore.QRect(30, 50, 119, 27))
        self.redBut.setObjectName("redBut")
        self.redBut.toggled.connect(lambda:self.btnstate(self.redBut))
        self.greenBut = QtWidgets.QRadioButton(Dialog)
        self.greenBut.setGeometry(QtCore.QRect(30, 100, 119, 27))
        self.greenBut.setObjectName("greenBut")
        self.greenBut.toggled.connect(lambda:self.btnstate(self.greenBut))
        self.blueBut = QtWidgets.QRadioButton(Dialog)
        self.blueBut.setGeometry(QtCore.QRect(30, 150, 119, 27))
        self.blueBut.setObjectName("blueBut")
        self.blueBut.toggled.connect(lambda:self.btnstate(self.blueBut))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Power lights RGB"))
        self.redBut.setText(_translate("Dialog", "Red"))
        self.greenBut.setText(_translate("Dialog", "Green"))
        self.blueBut.setText(_translate("Dialog", "Blue"))
    def btnstate(self, b):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(3, GPIO.OUT)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(7, GPIO.OUT)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(7, GPIO.LOW)
        if b.text() == "Red":
            if b.isChecked() == True:
                GPIO.output(3, GPIO.HIGH)
                GPIO.output(5, GPIO.LOW)
                GPIO.output(7, GPIO.LOW)
        if b.text() == "Green":
            if b.isChecked() == True:
                GPIO.output(3, GPIO.LOW)
                GPIO.output(5, GPIO.HIGH)
                GPIO.output(7, GPIO.LOW)
        if b.text() == "Blue":
            if b.isChecked() == True:
                GPIO.output(3, GPIO.LOW)
                GPIO.output(5, GPIO.LOW)
                GPIO.output(7, GPIO.HIGH)
       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    GPIO.cleanup()
