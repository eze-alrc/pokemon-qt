import sys
from PyQt5 import QtGui, QtWidgets
from pokemon import Ui_MainWindow  

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)  

        self.ui.pushButton.clicked.connect(self.verificar_resposta)

    def verificar_resposta(self):
        self.ui.label_3.setPixmap(QtGui.QPixmap("img/charmander.png"))
        self.ui.label_3.setScaledContents(True)

        self.ui.radioButton.setStyleSheet(f"color: darkred")
        self.ui.radioButton_2.setStyleSheet(f"color: darkred")
        self.ui.radioButton_3.setStyleSheet(f"color: darkred")
        self.ui.radioButton_4.setStyleSheet(f"color: green")
    
                

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())