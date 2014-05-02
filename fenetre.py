from PyQt5.QtWidgets import *
import sys
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
        numero_domaine = int(self.ui.textEdit.plainText())
        for i in range(taille_grille):
            for j in range(taille_grille):        
                if self.ui.checkBox_dict[(i,j)].isChecked():
                    liste_coordonnees.append((i,j))
        liste.append(numero_domaine)
        liste.append(liste_coordonnees)
        dico[reference] = liste
        reference += 1
 
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
    
