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
		requete = "SELECT texte  FROM chapitre WHERE no_chapitre = %s"
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
		mycursor2 = mydb.cursor()
		# Dans notre requête on remplace tous les paramêtres par des %s
		requete2 = "SELECT id  FROM arme WHERE  nom = %s"
		# Ensuite on crée un tuple avec les valeurs des paramêtres
		parametres2 = (self.plainTextEditAjoutArmes.toPlainText(),)
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor2.execute(requete2, parametres2)

		# Le curseur récupère toutes les données du résultat de la requête
		myresult2 = mycursor2.fetchall()
		id = str(myresult2)
		
		variable = id.replace('[', '').replace(']', '').replace('"', '').replace('(', "").replace(')', "").replace("'", "").replace(",", "")
		
		mycursor2.close()
		
		mycursor = mydb.cursor()
		nom = self.plainTextEditAjoutArmes.toPlainText()
		

		# Dans notre requête on remplace tous les paramêtres par des %s
		requete = "INSERT INTO lien_arme (id_feuille_aventure, id_arme) values (1, %s)"
		# Ensuite on crée un tuple avec les valeurs des paramêtres
		parametres = (int(variable),)
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor.execute(requete, parametres)
		mydb.commit()
		mycursor.close()
		
	def AjoutObjet(self):
		mycursor2 = mydb.cursor()
		# Dans notre requête on remplace tous les paramêtres par des %s
		requete2 = "SELECT id  FROM objet WHERE  nom = %s"
		# Ensuite on crée un tuple avec les valeurs des paramêtres
		parametres2 = (self.plainTextEditAjoutObjet.toPlainText(),)
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor2.execute(requete2, parametres2)

		# Le curseur récupère toutes les données du résultat de la requête
		myresult2 = mycursor2.fetchall()
		id = str(myresult2)
		
		variable = id.replace('[', '').replace(']', '').replace('"', '').replace('(', "").replace(')', "").replace("'", "").replace(",", "")
		
		mycursor2.close()
		
		mycursor = mydb.cursor()
		nom = self.plainTextEditAjoutObjet.toPlainText()
		

		# Dans notre requête on remplace tous les paramêtres par des %s
		requete = "INSERT INTO lien_objet (id_feuille_aventure, id_objet) values (1, %s)"
		# Ensuite on crée un tuple avec les valeurs des paramêtres
		parametres = (int(variable),)
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor.execute(requete, parametres)
		mydb.commit()
		mycursor.close()
	
	def FeuilleAventure(self):
		discipline1 = self.comboBoxDiscipline1.currentText()
		discipline2 = self.comboBoxDiscipline2.currentText()
		discipline3 = self.comboBoxDiscipline3.currentText()
		discipline4 = self.comboBoxDiscipline4.currentText()
		discipline5 = self.comboBoxDiscipline5.currentText()
		
		parametres1 = (discipline1,)
		parametres2 = (discipline2,)
		parametres3 = (discipline3,)
		parametres4 = (discipline4,)
		parametres5 = (discipline5,)
		
		mycursor = mydb.cursor()

		requete = "SELECT id  FROM discipline_kai WHERE  nom = %s"
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor.execute(requete, parametres1)

		# Le curseur récupère toutes les données du résultat de la requête
		myresult = mycursor.fetchall()
		id = str(myresult)
		
		variable1 = id.replace('[', '').replace(']', '').replace('"', '').replace('(', "").replace(')', "").replace("'", "").replace(",", "")
		
		# Dans notre requête on remplace tous les paramêtres par des %s
		requete6 = "INSERT INTO lien_discipline_kai (id_feuille_aventure, id_discipline_kai) values (1, %s)"
		# Ensuite on crée un tuple avec les valeurs des paramêtres
		parametres6 = (int(variable1),)
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor.execute(requete6, parametres6)
		mydb.commit()
		
		mycursor.close()

		mycursor2 = mydb.cursor()
		requete2 = "SELECT id  FROM discipline_kai WHERE  nom = %s"
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor2.execute(requete2, parametres2)

		# Le curseur récupère toutes les données du résultat de la requête
		myresult2 = mycursor2.fetchall()
		id = str(myresult2)
		
		variable2 = id.replace('[', '').replace(']', '').replace('"', '').replace('(', "").replace(')', "").replace("'", "").replace(",", "")
		
		# Dans notre requête on remplace tous les paramêtres par des %s
		requete7 = "INSERT INTO lien_discipline_kai (id_feuille_aventure, id_discipline_kai) values (1, %s)"
		# Ensuite on crée un tuple avec les valeurs des paramêtres
		parametres7 = (int(variable2),)
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor2.execute(requete7, parametres7)
		mydb.commit()
		
		mycursor2.close()
		
		mycursor3 = mydb.cursor()
		requete3 = "SELECT id  FROM discipline_kai WHERE  nom = %s"
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor3.execute(requete3, parametres3)

		# Le curseur récupère toutes les données du résultat de la requête
		myresult3 = mycursor3.fetchall()
		id = str(myresult3)
		
		variable3 = id.replace('[', '').replace(']', '').replace('"', '').replace('(', "").replace(')', "").replace("'", "").replace(",", "")
		
		# Dans notre requête on remplace tous les paramêtres par des %s
		requete8 = "INSERT INTO lien_discipline_kai (id_feuille_aventure, id_discipline_kai) values (1, %s)"
		# Ensuite on crée un tuple avec les valeurs des paramêtres
		parametres8 = (int(variable3),)
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor3.execute(requete8, parametres8)
		mydb.commit()
		
		mycursor3.close()
		
		mycursor4 = mydb.cursor()
		requete4 = "SELECT id  FROM discipline_kai WHERE  nom = %s"
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor4.execute(requete4, parametres4)

		# Le curseur récupère toutes les données du résultat de la requête
		myresult4 = mycursor4.fetchall()
		id = str(myresult4)
		
		variable4 = id.replace('[', '').replace(']', '').replace('"', '').replace('(', "").replace(')', "").replace("'", "").replace(",", "")
		
		# Dans notre requête on remplace tous les paramêtres par des %s
		requete9 = "INSERT INTO lien_discipline_kai (id_feuille_aventure, id_discipline_kai) values (1, %s)"
		# Ensuite on crée un tuple avec les valeurs des paramêtres
		parametres9 = (int(variable4),)
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor4.execute(requete9, parametres9)
		mydb.commit()
		
		mycursor4.close()
		
		mycursor5 = mydb.cursor()
		requete5 = "SELECT id  FROM discipline_kai WHERE  nom = %s"
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor5.execute(requete5, parametres5)

		# Le curseur récupère toutes les données du résultat de la requête
		myresult5 = mycursor5.fetchall()
		id = str(myresult5)
		
		variable5 = id.replace('[', '').replace(']', '').replace('"', '').replace('(', "").replace(')', "").replace("'", "").replace(",", "")
		
		# Dans notre requête on remplace tous les paramêtres par des %s
		requete10 = "INSERT INTO lien_discipline_kai (id_feuille_aventure, id_discipline_kai) values (1, %s)"
		# Ensuite on crée un tuple avec les valeurs des paramêtres
		parametres10 = (int(variable5),)
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor5.execute(requete10, parametres10)
		mydb.commit()
		
		mycursor5.close()
		
		
	def ModifBourse(self):
		mycursor = mydb.cursor()
		bourse = self.plainTextEditBoursesweesfd.toPlainText()
		self.Bourse.setText(str(bourse))
		mycursor = mydb.cursor()

		# Dans notre requête on remplace tous les paramêtres par des %s
		requete = "UPDATE feuille_aventure SET bourse = %s WHERE id = 1;"
		# Ensuite on crée un tuple avec les valeurs des paramêtres
		parametres = (bourse,)
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor.execute(requete, parametres)
		mydb.commit()
		mycursor.close()
		
	
	def ModifEndurance(self):
		mycursor = mydb.cursor()
		endurance = self.plainTextEditEndurance.toPlainText()
		self.Endurance.setText(str(endurance))
		mycursor = mydb.cursor()

		# Dans notre requête on remplace tous les paramêtres par des %s
		requete = "UPDATE feuille_aventure SET endurance = %s WHERE id = 1;"
		# Ensuite on crée un tuple avec les valeurs des paramêtres
		parametres = (endurance,)
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor.execute(requete, parametres)
		mydb.commit()
		mycursor.close()
	
	def ModifHabilete(self):
		mycursor = mydb.cursor()
		habilete = self.plainTextEditHabilete.toPlainText()
		self.Habilete.setText(str(habilete))
		mycursor = mydb.cursor()

		# Dans notre requête on remplace tous les paramêtres par des %s
		requete = "UPDATE feuille_aventure SET endurance = %s WHERE id = 1;"
		# Ensuite on crée un tuple avec les valeurs des paramêtres
		parametres = (habilete,)
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor.execute(requete, parametres)
		mydb.commit()
		mycursor.close()
	def SupprimerSauvegarde(self):
		print("bye")
	
	def Sauvegarde(self):
		mycursor = mydb.cursor()
		no_chapitre = self.chapitreNum.value()
		

		# Dans notre requête on remplace tous les paramêtres par des %s
		requete = "INSERT INTO sauvegarde (no_chapitre, feuille_aventure) values (%s, 1)"
		# Ensuite on crée un tuple avec les valeurs des paramêtres
		parametres = (int(no_chapitre),)
		
		# Dans le execute on passe en paramêtres la requête et ensuite les paramêtres
		mycursor.execute(requete, parametres)
		mydb.commit()
		mycursor.close()

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
