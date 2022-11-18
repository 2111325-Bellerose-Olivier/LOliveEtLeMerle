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
	
	def afficher_tout():
		print("allo")
	
	def __init__(self, *args, obj=None, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		# On va créer la fenêtre avec cette commande
		self.setupUi(self)
		
		mycursor = mydb.cursor()

		# Dans notre requête on remplace tous les paramêtres par des %s
		requete = "SELECT nom  FROM arme"
		# Ensuite on crée un tuple avec les valeurs des paramêtres

		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor.execute(requete)

		# Le curseur récupère toutes les données du résultat de la requête
		myresult = mycursor.fetchall()
		texte = str(myresult)
		
		
		for text in myresult:
			variable = texte.replace('[', '').replace(']', '').replace('"', '').replace('(', "").replace(')', "").replace("'", "")
			self.plainTextEditArmes.setPlainText(variable)
		mycursor.close()
		
		
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
		
		
	def AjoutArmes(self):
		mycursor = mydb.cursor()
		nom = self.plainTextEditAjoutArmes.toPlainText()
		
		mycursor = mydb.cursor()

		# Dans notre requête on remplace tous les paramêtres par des %s
		requete = "INSERT INTO arme (nom) values (%s)"
		# Ensuite on crée un tuple avec les valeurs des paramêtres
		parametres = (str(nom),)
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		if mycursor.execute(requete, parametres):
			print("fonctionne")
		mycursor.close()
		
	def AjoutObjet(self):
		mycursor = mydb.cursor()
		nom = self.plainTextEditAjoutObjet.toPlainText()
		
		mycursor = mydb.cursor()

		# Dans notre requête on remplace tous les paramêtres par des %s
		requete = "INSERT INTO objet (nom_objet) values (%s)"
		# Ensuite on crée un tuple avec les valeurs des paramêtres
		parametres = (nom,)
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor.execute(requete, parametres)
		mycursor.close()
	
	def FeuilleAventure(self):
	print("60")
	def ModifBourse(self):
		mycursor = mydb.cursor()
		bourse = self.plainTextEditBourse.toPlainText()
		
		mycursor = mydb.cursor()

		# Dans notre requête on remplace tous les paramêtres par des %s
		requete = "UPDATE feuille_aventure SET bourse = %s WHERE id = 1;"
		# Ensuite on crée un tuple avec les valeurs des paramêtres
		parametres = (bourse,)
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor.execute(requete, parametres)
		mycursor.close()
	
	def ModifEndurance(self):
		mycursor = mydb.cursor()
		endurance = self.plainTextEditEndurance.toPlainText()
		
		mycursor = mydb.cursor()

		# Dans notre requête on remplace tous les paramêtres par des %s
		requete = "UPDATE feuille_aventure SET endurance = %s WHERE id = 1;"
		# Ensuite on crée un tuple avec les valeurs des paramêtres
		parametres = (endurance,)
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor.execute(requete, parametres)
		mycursor.close()
	
	def ModifHabilete(self):
		mycursor = mydb.cursor()
		habilete = self.plainTextEditHabilete.toPlainText()
		
		mycursor = mydb.cursor()

		# Dans notre requête on remplace tous les paramêtres par des %s
		requete = "UPDATE feuille_aventure SET endurance = %s WHERE id = 1;"
		# Ensuite on crée un tuple avec les valeurs des paramêtres
		parametres = (habilete,)
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor.execute(requete, parametres)
		mycursor.close()

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
