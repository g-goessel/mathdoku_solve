from PyQt5.QtWidgets import *
import sys
from t import *
from t2 import *

global taille_grille
taille_grille = 1

class FenetrePrincipal(QDialog):
    def __init__(self, parent=None):
        super(FenetrePrincipal, self).__init__(parent)
        self.createWidgets()
 
    def createWidgets(self):
        self.ui = Ui_Principal()
        self.ui.setupUi(self)
 
class MathDoku(QDialog):

    def __init__(self, parent=None):
        super(MathDoku, self).__init__(parent)
        self.createWidgets()
 
    def createWidgets(self):
        self.ui = Ui_MathDoku()
        self.ui.setupUi(self)

		
    def print_lable(self,x):
        global taille_grille
        taille_grille = x
    
    def clique_ok(self):
        self.close()
        self.screen2 = FenetrePrincipal()
        self.screen2.show()
		
if __name__=='__main__':

    
 
    app = QApplication(sys.argv)
 
    screen = MathDoku()
    screen.show()

    app.exec_()
    print(taille_grille)
    