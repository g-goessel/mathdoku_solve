from PyQt5.QtWidgets import *
from PyQt5 import *
import sys
import pickle
from t import *
from t2 import *

class FenetrePrincipal(QDialog):
    global taille_grille
    global dico
    global reference
    reference = 1
    taille_grille=dict()
    dico = dict()
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
                    liste_coordonnees.append((i+1,j+1))
        liste.append(numero_domaine)
        liste.append(liste_coordonnees)
        dico[reference] = liste
        print(dico[reference])
        reference += 1
    
    def enregistrer_grille(self):
        global dico
        urlbis = QFileDialog.getSaveFileName(self, "Enregistrer une grille", '.', "Grille MathDoku(pas d'extension)")
        url = urlbis[0]
        nom_fichier = url.split("/")[6]
        with open(nom_fichier, 'wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(dico)
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
		
if __name__=='__main__':    
 
    app = QApplication(sys.argv)
 
    screen = MathDoku()
    screen.show()

    app.exec_()
    
