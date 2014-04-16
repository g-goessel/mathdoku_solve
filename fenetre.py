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
 
if __name__=='__main__':
    import sys
 
    app = QApplication(sys.argv)
 
    screen = MathDoku()
    screen.show()
 
    sys.exit(app.exec_())