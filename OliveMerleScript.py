import sys
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="merlive"
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
		
		self.buttonChapitre.clicked.connect(self.GoChapitre)
		
		self.buttonProchainChapitre.clicked.connect(self.ProchainChapitre)
		
	def GoChapitre(self):
		self.plainTextEdit.setPlainText("")
		
		# Création d'un curseur
		mycursor = mydb.cursor()

		# Dans notre requête on remplace tous les paramêtres par des %s
		requete = "SELECT texte  FROM chapitre WHERE no_chapitre = %s limit 2,1"
		# Ensuite on crée un tuple avec les valeurs des paramêtres
		parametres = (self.chapitreNum.value(),)
		
		chapitre_actuel = self.chapitreNum.value()
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor.execute(requete, parametres)

		# Le curseur récupère toutes les données du résultat de la requête
		myresult = mycursor.fetchall()
		texte = str(myresult)
		
		variable = texte.replace('[', '').replace(']', '').replace('"', '').replace('(', '',1)
		
		self.plainTextEdit.setPlainText(variable)
		mycursor.close()
		
		mycursor = mydb.cursor()
		# Dans notre requête on remplace tous les paramêtres par des %s
		requete2 = "SELECT no_chapitre_destination  FROM lien_chapitre WHERE no_chapitre_origine = %s"
		
		parametres2 = (chapitre_actuel,)
		
		mycursor.execute(requete2, parametres2)
		
		myresult2 = mycursor.fetchall()
		
		print(chapitre_actuel)
		index =0
		self.ProchainComboBox.setItemText(0, "")
		self.ProchainComboBox.setItemText(1, "")
		self.ProchainComboBox.setItemText(2, "")
		
		for(no_chapitre_destination ) in myresult2:
			variable = str(no_chapitre_destination).replace('(', '').replace(')', '').replace(',', '')
			self.ProchainComboBox.setItemText(index, str(variable))
			index = index + 1
			print(self.ProchainComboBox.currentText())
			
		
	def ProchainChapitre(self):
		print("3")

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
