# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created: Wed Apr 16 17:23:08 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import fenetre

class Ui_Principal(object):

    def __init__(self,a):
        global taille_grille
        taille_grille=a[1]

    def setupUi(self, Principal):
        """
        checkBox_dict contient les coordonnées de toutes les checkboxes sous la forme 'i_j':(position_x,position_y,20,17) 
        20 correspond à la largeur
        17 correspond à la hauteur
        """
        global taille_grille
        self.checkBox_dict=dict()
        for i in range(taille_grille):
            for j in range(taille_grille):
                self.checkBox_dict[(i,j)]=(30+30*i,30+30*j,20,17)

        largeur=max(450,250+50*taille_grille)
        longueur = max(200,60+30*taille_grille)

        Principal.setObjectName("Principal")
        Principal.resize(largeur,longueur)
        
        self.buttonBox = QtWidgets.QDialogButtonBox(Principal)
        self.buttonBox.setGeometry(QtCore.QRect(30, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.liste_check = []
        for i in range(taille_grille):
            liste_i = []
            for j in range(taille_grille): 
                self.checkBox= QtWidgets.QCheckBox(Principal)
                self.checkBox.setGeometry(QtCore.QRect(*self.checkBox_dict[(i,j)]))
                self.checkBox.setText("")
                self.checkBox.setObjectName('checkBox' + str(i) + str(j))
                liste_i.append(self.checkBox)
            self.liste_check.append(liste_i)
        self.textEdit = QtWidgets.QTextEdit(Principal)
        self.textEdit.setGeometry(QtCore.QRect(largeur-270, 30, 104, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_4 = QtWidgets.QPushButton(Principal)
        self.pushButton_4.setGeometry(QtCore.QRect(largeur-140, 30, 131, 16))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(Principal)
        self.pushButton.setGeometry(QtCore.QRect(160, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Principal)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 90, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Principal)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 90, 95, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Principal)
        self.pushButton_4.clicked.connect(Principal.domaine)
        self.pushButton_3.clicked.connect(Principal.enregistrer_grille)
        self.buttonBox.rejected.connect(Principal.reject)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "Dialog"))
        self.pushButton.setText(_translate("Principal", "Résoudre"))
        self.pushButton_2.setText(_translate("Principal", "Effacer"))
        self.pushButton_3.setText(_translate("Principal", "Enregister"))
        self.pushButton_4.setText(_translate("Principal", "Domaine OK"))
        
