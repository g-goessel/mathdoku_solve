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
        self.pushButton_4.setGeometry(QtCore.QRect(largeur-140, 35, 131, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(Principal)
        self.pushButton.setGeometry(QtCore.QRect(largeur-80, longueur - 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Principal)
        self.pushButton_2.setGeometry(QtCore.QRect(largeur - 160, longueur - 30, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        
        ###                     MENU                        ###
        
        self.menubar = QtWidgets.QMenuBar(Principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.statusbar = QtWidgets.QStatusBar(Principal)
        self.statusbar.setObjectName("statusbar")
        self.ouvrir_grille = QtWidgets.QAction(Principal)
        self.ouvrir_grille.setObjectName("ouvrir_grille")
        self.enregistrer_grille = QtWidgets.QAction(Principal)
        self.enregistrer_grille.setObjectName("ouvrir_grille")
        self.menuFichier.addAction(self.ouvrir_grille)
        self.menuFichier.addAction(self.enregistrer_grille)
        self.menubar.addAction(self.menuFichier.menuAction())
        
        ###                     MENU                        ###
        
        self.retranslateUi(Principal)
        self.ouvrir_grille.triggered.connect(Principal.ouvrir_grille)
        self.enregistrer_grille.triggered.connect(Principal.enregistrer_grille)
        self.pushButton_4.clicked.connect(Principal.domaine)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
    
        global taille_grille 
        
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "Résolution du MathDoku de taille " + str(taille_grille) + 'x' + str(taille_grille)))
        self.pushButton.setText(_translate("Principal", "Résoudre"))
        self.pushButton_2.setText(_translate("Principal", "Effacer"))
        self.pushButton_4.setText(_translate("Principal", "Valider"))
        self.menuFichier.setTitle(_translate("Principal", "Options"))
        self.ouvrir_grille.setText(_translate("Principal", "Ouvrir une grille"))
        self.enregistrer_grille.setText(_translate("Principal", "Enregistrer une grille"))