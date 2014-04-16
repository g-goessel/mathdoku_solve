# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created: Wed Apr 16 17:23:08 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Principal(object):
    def setupUi(self, Principal):
        """
        checkBox_dict contient les coordonnées de toutes les checkboxes sous la forme 'i_j':(x,y,20,17) 
        20 correspond à la largeur et 17 à ?
        """

        taille_grille=4

        checkBox_dict=dict()
        for i in range(taille_grille):
            for j in range(taille_grille):
                checkBox_dict[str(i)+'_'+str(j)]=(30+30*i,30+30*j,20,17)


        Principal.setObjectName("Principal")
        Principal.resize(800, 800)
        self.buttonBox = QtWidgets.QDialogButtonBox(Principal)
        self.buttonBox.setGeometry(QtCore.QRect(30, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        for checkBox in checkBox_dict:
            self.checkBox = QtWidgets.QCheckBox(Principal)
            self.checkBox.setGeometry(QtCore.QRect(*checkBox_dict[checkBox]))
            self.checkBox.setText("")
            self.checkBox.setObjectName("checkBox")

            
        # self.checkBox_2 = QtWidgets.QCheckBox(Principal)
        # self.checkBox_2.setGeometry(QtCore.QRect(30, 50, 20, 17))
        # self.checkBox_2.setText("")
        # self.checkBox_2.setObjectName("checkBox_2")
        # self.checkBox_3 = QtWidgets.QCheckBox(Principal)
        # self.checkBox_3.setGeometry(QtCore.QRect(30, 80, 70, 17))
        # self.checkBox_3.setText("")
        # self.checkBox_3.setObjectName("checkBox_3")
        # self.checkBox_4 = QtWidgets.QCheckBox(Principal)
        # self.checkBox_4.setGeometry(QtCore.QRect(60, 20, 70, 17))
        # self.checkBox_4.setText("")
        # self.checkBox_4.setObjectName("checkBox_4")
        # self.checkBox_5 = QtWidgets.QCheckBox(Principal)
        # self.checkBox_5.setGeometry(QtCore.QRect(60, 50, 70, 17))
        # self.checkBox_5.setText("")
        # self.checkBox_5.setObjectName("checkBox_5")
        # self.checkBox_6 = QtWidgets.QCheckBox(Principal)
        # self.checkBox_6.setGeometry(QtCore.QRect(60, 80, 70, 17))
        # self.checkBox_6.setText("")
        # self.checkBox_6.setObjectName("checkBox_6")
        # self.checkBox_7 = QtWidgets.QCheckBox(Principal)
        # self.checkBox_7.setGeometry(QtCore.QRect(90, 80, 70, 17))
        # self.checkBox_7.setText("")
        # self.checkBox_7.setObjectName("checkBox_7")
        # self.checkBox_8 = QtWidgets.QCheckBox(Principal)
        # self.checkBox_8.setGeometry(QtCore.QRect(90, 50, 70, 17))
        # self.checkBox_8.setText("")
        # self.checkBox_8.setObjectName("checkBox_8")
        # self.checkBox_9 = QtWidgets.QCheckBox(Principal)
        # self.checkBox_9.setGeometry(QtCore.QRect(90, 20, 70, 17))
        # self.checkBox_9.setText("")
        # self.checkBox_9.setObjectName("checkBox_9")
        self.textEdit = QtWidgets.QTextEdit(Principal)
        self.textEdit.setGeometry(QtCore.QRect(150, 30, 104, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Principal)
        self.label.setGeometry(QtCore.QRect(270, 30, 131, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Principal)
        self.pushButton.setGeometry(QtCore.QRect(150, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Principal)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 90, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Principal)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 90, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Principal)
        self.buttonBox.accepted.connect(Principal.accept)
        self.buttonBox.rejected.connect(Principal.reject)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "Dialog"))
        self.label.setText(_translate("Principal", "Résolution du MathDoku"))
        self.pushButton.setText(_translate("Principal", "Résoudre"))
        self.pushButton_2.setText(_translate("Principal", "Effacer"))
        self.pushButton_3.setText(_translate("Principal", "Enregister..."))

