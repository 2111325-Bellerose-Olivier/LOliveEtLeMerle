import sys
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password=""
)

print(mydb)

from PyQt5.QtWidgets import QApplication, QMainWindow
# Importer la classe Ui_MainWindow du fichier MainWindow.py
from FenetreOliveMerle import Ui_MainWindow

# En paramêtre de la classe MainWindow on va hériter des fonctionnalités
# de QMainWindow et de notre interface Ui_MainWindow
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # On va créer la fenêtre avec cette commande
        self.setupUi(self)

  
app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
