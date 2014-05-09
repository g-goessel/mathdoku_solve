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

    def retranslateUi(self, Resultat):
        _translate = QtCore.QCoreApplication.translate
        Resultat.setWindowTitle(_translate("Resultat", "Resultat"))

