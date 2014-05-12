from PyQt5.QtWidgets import *
from PyQt5 import *
import sys
import pickle
from t import *
from t2 import *
from fonctions import *
from bruteforce import *
from t3 import *

class FenetrePrincipal(QDialog):
    global taille_grille
    global dico
    global reference
    global resultat
    reference = 0
    taille_grille=dict()
    dico = dict()
    resultat = dict()
    def __init__(self,parametres ,parent=None):
        global taille_grille
        taille_grille=parametres
        super(FenetrePrincipal, self).__init__(parent)
        self.createWidgets()
 
    def createWidgets(self):
        global taille_grille
        self.ui = Ui_Principal(taille_grille)
        self.ui.setupUi(self)

    def domaine(self):
        global taille_grille
        global dico
        global reference
        liste_coordonnees = []
        liste = []
        numero_domaine = int(self.ui.textEdit.toPlainText())
        for i in range(taille_grille[1]):
            for j in range(taille_grille[1]): 
                checkBox = self.ui.liste_check[i][j]
                if checkBox.isChecked():
                    checkBox.setChecked(False)
                    checkBox.setCheckable(False)
                    checkBox.hide()
                    liste_coordonnees.append((i,j))
        liste.append(numero_domaine)
        liste.append(liste_coordonnees)
        dico[reference] = liste
        print(dico[reference])
        reference += 1
    
    def enregistrer_grille(self):
        global dico
        urlbis = QFileDialog.getSaveFileName(self, "Enregistrer une grille", '.', "Grille MathDoku(*mtku)")
        url = urlbis[0]
        split = url.split("/")
        print(split)
        nom_fichier = split[len(split)-1]
        with open(nom_fichier + str('.mtku'), 'wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(dico)

    def ouvrir_grille(self):
        global dico
        urlbis = QFileDialog.getOpenFileName(self,"Ouvrir une grille", '.', "Grille MathDoku(*mtku)")
        url = urlbis[0]
        print(url)
        split = url.split("/")
        nom_fichier = split[len(split)-1]
        with open(nom_fichier, 'rb') as fichier:
            mon_depickler = pickle.Unpickler(fichier)
            dico = mon_depickler.load()
        print(dico)
        
    def resolution(self):
        global dico
        global taille_grille
        global resultat
        for element in range(len(dico)):
            valeur = dico[element][0]
            nbr_cases = len(dico[element][1])
            dico[element].append(combi_possibles(valeur,nbr_cases,taille_grille[1]))
            
        print(dico)
        optimize(dico)
        optimize(dico)
        optimize(dico)
        resultat=bruteforce(dico,taille_grille[1])
        if resultat != (False,'Pas de solution touvée') :
            self.afficher_resultat()
        print(resultat)    

    def afficher_resultat(self):
        global taille_grille  
        global resultat
        self.screen3 = Resultat(taille_grille, resultat)
        self.screen3.show()    
class MathDoku(QDialog):
    #global taille_grille
    taille_grille=dict()

    def __init__(self, parent=None):
        super(MathDoku, self).__init__(parent)
        self.createWidgets()
 
    def createWidgets(self):
        self.ui = Ui_MathDoku()
        self.ui.setupUi(self)

    def export_taille(self,x):
        #global taille_grille
        self.taille_grille[1] = x
    
    def clique_ok(self):
        self.close()
        self.screen2 = FenetrePrincipal(self.taille_grille)
        self.screen2.show()

class Resultat(QDialog):
    global taille_grille
    global resultat
    
    taille_grille = dict()
    resultat = dict()
    
    def __init__(self,taille, result ,parent=None):
        global taille_grille
        global resultat
        taille_grille= taille
        resultat = result
        super(Resultat, self).__init__(parent)
        self.createWidgets()

    def createWidgets(self):
        global taille_grille
        global resultat
        self.ui = Ui_Resultat(taille_grille, resultat)
        self.ui.setupUi(self)


if __name__=='__main__':    
 
    app = QApplication(sys.argv)
 
    screen = MathDoku()
    screen.show()

    app.exec_()
    
