# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Fri May  9 12:36:55 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from fenetre import *

class Ui_Resultat(object):

    def __init__(self, taille, result):
        global taille_grille
        global resultat
        taille_grille = taille[1]
        resultat = result

    def setupUi(self, Resultat):
        global taille_grille
        global resultat
        Resultat.setObjectName("Resultat")
        Resultat.resize(taille_grille*40, taille_grille*40)
        self.retranslateUi(Resultat)
        QtCore.QMetaObject.connectSlotsByName(Resultat)
        self.centralwidget = QtWidgets.QWidget(Resultat)
        self.centralwidget.setObjectName("centralwidget")
        verticaux = []
        horizontaux = []
        for horizontal in range(1,taille_grille):
            self.horizon = QtWidgets.QFrame(self.centralwidget)
            self.horizon.setGeometry(QtCore.QRect(0, horizontal*40, taille_grille*40, 3))
            self.horizon.setFrameShape(QtWidgets.QFrame.HLine)
            self.horizon.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.horizon.setObjectName("horizon" + str(horizontal))
            horizontaux.append(self.horizon)
            self.vertic = QtWidgets.QFrame(self.centralwidget)
            self.vertic.setGeometry(QtCore.QRect(horizontal*40, 0, 3, taille_grille*40))
            self.vertic.setFrameShape(QtWidgets.QFrame.VLine)
            self.vertic.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.vertic.setObjectName("vertic" + str(horizontal))
            verticaux.append(self.vertic)
         
       
    def retranslateUi(self, Resultat):
        _translate = QtCore.QCoreApplication.translate
        Resultat.setWindowTitle(_translate("Resultat", "Resultat"))

