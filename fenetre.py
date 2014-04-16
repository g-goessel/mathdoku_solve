from PyQt5.QtWidgets import *
import sys
from t import *
from t2 import *

class FenetrePrincipal(QDialog):
    def __init__(self, parent=None):
        super(FenetrePrincipal, self).__init__(parent)
        self.createWidgets()
 
    def createWidgets(self):
        self.ui = Ui_Principal()
        self.ui.setupUi(self)
 
class MathDoku(QDialog):
    global taille_grille
    taille_grille=int()

    def __init__(self, parent=None):
        super(MathDoku, self).__init__(parent)
        self.createWidgets()
 
    def createWidgets(self):
        self.ui = Ui_MathDoku()
        self.ui.setupUi(self)

		
    def export_taille(self,x):
        global taille_grille
        taille_grille = x
        print(x)
    
    def clique_ok(self):
        global taille_grille
        self.close()
        print(taille_grille)
        self.screen2 = FenetrePrincipal()
        self.screen2.show()

    def return_taille_grille():
        global taille_grille
        return taille_grille
		
if __name__=='__main__':

    
 
    app = QApplication(sys.argv)
 
    screen = MathDoku()
    screen.show()

    app.exec_()
    #print(taille_grille)
    