from PyQt5.QtWidgets import *
import sys
from t import *
from t2 import *

class FenetrePrincipal(QDialog):
    global taille_grille
    taille_grille=dict()
    def __init__(self,parametres ,parent=None):
        global taille_grille
        taille_grille=parametres
        print('FenetrePrincipale',parametres)
        super(FenetrePrincipal, self).__init__(parent)
        self.createWidgets()
 
    def createWidgets(self):
        global taille_grille
        self.ui = Ui_Principal(taille_grille)
        self.ui.setupUi(self)
 
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
        print(x)
    
    def clique_ok(self):
        self.close()
        print(self.taille_grille)
        self.screen2 = FenetrePrincipal(self.taille_grille)
        self.screen2.show()
		
if __name__=='__main__':    
 
    app = QApplication(sys.argv)
 
    screen = MathDoku()
    screen.show()

    app.exec_()
    print(MathDoku.taille_grille)
    