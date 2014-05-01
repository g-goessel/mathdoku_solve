# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Wed Apr 16 16:28:01 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MathDoku(object):
    def setupUi(self, MathDoku):
        MathDoku.setObjectName("MathDoku")
        MathDoku.resize(499, 92)
        # MathDoku.setStyleSheet("font: 8pt \"Comic Sans MS\";")
        self.horizontalSlider = QtWidgets.QSlider(MathDoku)
        self.horizontalSlider.setGeometry(QtCore.QRect(50, 50, 160, 22))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(9)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(MathDoku)
        self.buttonBox_2.setGeometry(QtCore.QRect(320, 60, 156, 23))
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.label = QtWidgets.QLabel(MathDoku)
        self.label.setGeometry(QtCore.QRect(50, 10, 46, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MathDoku)
        self.label_2.setGeometry(QtCore.QRect(15, 9, 341, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MathDoku)
        self.label_3.setGeometry(QtCore.QRect(240, 50, 41, 20))
        # self.label_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(MathDoku)
        self.buttonBox_2.accepted.connect(MathDoku.clique_ok)
        self.buttonBox_2.rejected.connect(MathDoku.close)
        self.horizontalSlider.valueChanged['int'].connect(self.label_3.setNum)
        self.horizontalSlider.valueChanged['int'].connect(MathDoku.export_taille)
        QtCore.QMetaObject.connectSlotsByName(MathDoku)

    def retranslateUi(self, MathDoku):
        _translate = QtCore.QCoreApplication.translate
        MathDoku.setWindowTitle(_translate("MathDoku", "Dialog"))
        self.label_2.setText(_translate("MathDoku", "<html><head/><body><p><span style=\" font-size:12pt;\">Veuillez entrer la taille de la grille à résoudre</span></p></body></html>"))
        self.label_3.setText(_translate("MathDoku", "1"))

