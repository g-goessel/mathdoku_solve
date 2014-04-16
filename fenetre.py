from PyQt5.QtWidgets import *
import sys
from t import *
 
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
 
if __name__=='__main__':

    
 
    app = QApplication(sys.argv)
 
    screen = MathDoku()
    screen.show()
    
    
    app.exec_()
    print(taille_grille)
    