# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 968)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chapitre = QtWidgets.QScrollArea(self.centralwidget)
        self.chapitre.setGeometry(QtCore.QRect(480, 50, 261, 51))
        self.chapitre.setWidgetResizable(True)
        self.chapitre.setObjectName("chapitre")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 259, 49))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.buttonChapitre = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.buttonChapitre.setGeometry(QtCore.QRect(160, 20, 75, 23))
        self.buttonChapitre.setObjectName("buttonChapitre")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.label.setObjectName("label")
        self.chapitreNum = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.chapitreNum.setGeometry(QtCore.QRect(90, 20, 61, 22))
        self.chapitreNum.setMaximum(148)
        self.chapitreNum.setObjectName("chapitreNum")
        self.chapitre.setWidget(self.scrollAreaWidgetContents)
        self.sauvegarde = QtWidgets.QScrollArea(self.centralwidget)
        self.sauvegarde.setGeometry(QtCore.QRect(910, 0, 181, 51))
        self.sauvegarde.setWidgetResizable(True)
        self.sauvegarde.setObjectName("sauvegarde")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 179, 49))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.buttonSauvegarde = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.buttonSauvegarde.setGeometry(QtCore.QRect(90, 10, 75, 23))
        self.buttonSauvegarde.setObjectName("buttonSauvegarde")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.label_4.setObjectName("label_4")
        self.sauvegarde.setWidget(self.scrollAreaWidgetContents_2)
        self.chapitre_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.chapitre_2.setGeometry(QtCore.QRect(480, 0, 431, 51))
        self.chapitre_2.setWidgetResizable(True)
        self.chapitre_2.setObjectName("chapitre_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 429, 49))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.buttonLivre = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.buttonLivre.setGeometry(QtCore.QRect(320, 10, 75, 23))
        self.buttonLivre.setObjectName("buttonLivre")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label_5.setObjectName("label_5")
        self.comboBoxLivre = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBoxLivre.setGeometry(QtCore.QRect(90, 10, 211, 22))
        self.comboBoxLivre.setObjectName("comboBoxLivre")
        self.comboBoxLivre.addItem("")
        self.chapitre_2.setWidget(self.scrollAreaWidgetContents_3)
        self.chapitre_3 = QtWidgets.QScrollArea(self.centralwidget)
        self.chapitre_3.setGeometry(QtCore.QRect(740, 50, 351, 51))
        self.chapitre_3.setWidgetResizable(True)
        self.chapitre_3.setObjectName("chapitre_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 349, 49))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.buttonSuppSauvegarde = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.buttonSuppSauvegarde.setGeometry(QtCore.QRect(260, 10, 75, 23))
        self.buttonSuppSauvegarde.setObjectName("buttonSuppSauvegarde")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 131, 31))
        self.label_6.setObjectName("label_6")
        self.comboBoxSuppSauvegarde = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        self.comboBoxSuppSauvegarde.setGeometry(QtCore.QRect(130, 10, 111, 21))
        self.comboBoxSuppSauvegarde.setObjectName("comboBoxSuppSauvegarde")
        self.chapitre_3.setWidget(self.scrollAreaWidgetContents_4)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 50, 481, 861))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 481, 51))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 479, 49))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_8.setGeometry(QtCore.QRect(200, 0, 61, 51))
        self.label_8.setObjectName("label_8")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_5)
        self.chapitre_4 = QtWidgets.QScrollArea(self.centralwidget)
        self.chapitre_4.setGeometry(QtCore.QRect(480, 100, 381, 51))
        self.chapitre_4.setWidgetResizable(True)
        self.chapitre_4.setObjectName("chapitre_4")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 379, 49))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 161, 31))
        self.label_9.setObjectName("label_9")
        self.buttonProchainChapitre = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.buttonProchainChapitre.setGeometry(QtCore.QRect(290, 10, 75, 23))
        self.buttonProchainChapitre.setObjectName("buttonProchainChapitre")
        self.ProchainComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents_6)
        self.ProchainComboBox.setGeometry(QtCore.QRect(170, 10, 111, 21))
        self.ProchainComboBox.setObjectName("ProchainComboBox")
        self.ProchainComboBox.addItem("")
        self.ProchainComboBox.setItemText(0, "")
        self.ProchainComboBox.addItem("")
        self.ProchainComboBox.setItemText(1, "")
        self.ProchainComboBox.addItem("")
        self.ProchainComboBox.setItemText(2, "")
        self.chapitre_4.setWidget(self.scrollAreaWidgetContents_6)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(480, 150, 631, 761))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 629, 759))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 161, 41))
        self.label_2.setObjectName("label_2")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_7)
        self.scrollArea_3.setGeometry(QtCore.QRect(0, 40, 351, 241))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 349, 239))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 131, 31))
        self.label_3.setObjectName("label_3")
        self.plainTextEditDiscipline1 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_8)
        self.plainTextEditDiscipline1.setGeometry(QtCore.QRect(0, 30, 131, 31))
        self.plainTextEditDiscipline1.setObjectName("plainTextEditDiscipline1")
        self.plainTextEditDiscipline2 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_8)
        self.plainTextEditDiscipline2.setGeometry(QtCore.QRect(0, 70, 131, 31))
        self.plainTextEditDiscipline2.setObjectName("plainTextEditDiscipline2")
        self.plainTextEditDiscipline3 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_8)
        self.plainTextEditDiscipline3.setGeometry(QtCore.QRect(0, 110, 131, 31))
        self.plainTextEditDiscipline3.setObjectName("plainTextEditDiscipline3")
        self.plainTextEditDiscipline4 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_8)
        self.plainTextEditDiscipline4.setGeometry(QtCore.QRect(0, 150, 131, 31))
        self.plainTextEditDiscipline4.setObjectName("plainTextEditDiscipline4")
        self.plainTextEditDiscipline5 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_8)
        self.plainTextEditDiscipline5.setGeometry(QtCore.QRect(0, 190, 131, 31))
        self.plainTextEditDiscipline5.setObjectName("plainTextEditDiscipline5")
        self.ButtonDiscipline = QtWidgets.QPushButton(self.scrollAreaWidgetContents_8)
        self.ButtonDiscipline.setGeometry(QtCore.QRect(260, 50, 75, 131))
        self.ButtonDiscipline.setObjectName("ButtonDiscipline")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_7.setGeometry(QtCore.QRect(150, 10, 47, 13))
        self.label_7.setObjectName("label_7")
        self.plainTextEditDisciplineNotes1 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_8)
        self.plainTextEditDisciplineNotes1.setGeometry(QtCore.QRect(150, 30, 104, 31))
        self.plainTextEditDisciplineNotes1.setObjectName("plainTextEditDisciplineNotes1")
        self.plainTextEditDisciplineNotes2 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_8)
        self.plainTextEditDisciplineNotes2.setGeometry(QtCore.QRect(150, 70, 104, 31))
        self.plainTextEditDisciplineNotes2.setObjectName("plainTextEditDisciplineNotes2")
        self.plainTextEditDisciplineNotes3 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_8)
        self.plainTextEditDisciplineNotes3.setGeometry(QtCore.QRect(150, 110, 104, 31))
        self.plainTextEditDisciplineNotes3.setObjectName("plainTextEditDisciplineNotes3")
        self.plainTextEditDisciplineNotes4 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_8)
        self.plainTextEditDisciplineNotes4.setGeometry(QtCore.QRect(150, 150, 104, 31))
        self.plainTextEditDisciplineNotes4.setObjectName("plainTextEditDisciplineNotes4")
        self.plainTextEditDisciplineNotes5 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_8)
        self.plainTextEditDisciplineNotes5.setGeometry(QtCore.QRect(150, 190, 104, 31))
        self.plainTextEditDisciplineNotes5.setObjectName("plainTextEditDisciplineNotes5")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_8)
        self.scrollArea_5 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_7)
        self.scrollArea_5.setGeometry(QtCore.QRect(350, 40, 271, 151))
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_10 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 269, 149))
        self.scrollAreaWidgetContents_10.setObjectName("scrollAreaWidgetContents_10")
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label_11.setObjectName("label_11")
        self.plainTextEditArmes1 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_10)
        self.plainTextEditArmes1.setGeometry(QtCore.QRect(10, 40, 81, 31))
        self.plainTextEditArmes1.setObjectName("plainTextEditArmes1")
        self.plainTextEditArmes2 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_10)
        self.plainTextEditArmes2.setGeometry(QtCore.QRect(10, 100, 81, 31))
        self.plainTextEditArmes2.setObjectName("plainTextEditArmes2")
        self.ButtonArmes = QtWidgets.QPushButton(self.scrollAreaWidgetContents_10)
        self.ButtonArmes.setGeometry(QtCore.QRect(190, 10, 75, 131))
        self.ButtonArmes.setObjectName("ButtonArmes")
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_12.setGeometry(QtCore.QRect(100, 10, 47, 13))
        self.label_12.setObjectName("label_12")
        self.plainTextEditArmesNotes1 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_10)
        self.plainTextEditArmesNotes1.setGeometry(QtCore.QRect(100, 40, 81, 31))
        self.plainTextEditArmesNotes1.setObjectName("plainTextEditArmesNotes1")
        self.plainTextEditArmesNotes2 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_10)
        self.plainTextEditArmesNotes2.setGeometry(QtCore.QRect(100, 100, 81, 31))
        self.plainTextEditArmesNotes2.setObjectName("plainTextEditArmesNotes2")
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_10)
        self.scrollArea_6 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_7)
        self.scrollArea_6.setGeometry(QtCore.QRect(0, 280, 631, 361))
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_11 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_11.setGeometry(QtCore.QRect(0, 0, 629, 359))
        self.scrollAreaWidgetContents_11.setObjectName("scrollAreaWidgetContents_11")
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)
        self.label_13.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label_13.setObjectName("label_13")
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)
        self.label_18.setGeometry(QtCore.QRect(80, 10, 171, 16))
        self.label_18.setObjectName("label_18")
        self.scrollArea_7 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_11)
        self.scrollArea_7.setGeometry(QtCore.QRect(0, 30, 331, 311))
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_12 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_12.setGeometry(QtCore.QRect(0, 0, 329, 309))
        self.scrollAreaWidgetContents_12.setObjectName("scrollAreaWidgetContents_12")
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.label_14.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label_14.setObjectName("label_14")
        self.comboBoxObjet1 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_12)
        self.comboBoxObjet1.setGeometry(QtCore.QRect(10, 70, 69, 22))
        self.comboBoxObjet1.setObjectName("comboBoxObjet1")
        self.comboBoxObjet1.addItem("")
        self.comboBoxObjet1.addItem("")
        self.comboBoxObjet1.addItem("")
        self.NumObjet1 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_12)
        self.NumObjet1.setGeometry(QtCore.QRect(100, 70, 61, 22))
        self.NumObjet1.setMaximum(8)
        self.NumObjet1.setObjectName("NumObjet1")
        self.plainTextEditObjet1 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_12)
        self.plainTextEditObjet1.setGeometry(QtCore.QRect(170, 60, 104, 31))
        self.plainTextEditObjet1.setObjectName("plainTextEditObjet1")
        self.plainTextEditObjet2 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_12)
        self.plainTextEditObjet2.setGeometry(QtCore.QRect(170, 90, 104, 31))
        self.plainTextEditObjet2.setObjectName("plainTextEditObjet2")
        self.plainTextEditObjet3 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_12)
        self.plainTextEditObjet3.setGeometry(QtCore.QRect(170, 120, 104, 31))
        self.plainTextEditObjet3.setObjectName("plainTextEditObjet3")
        self.plainTextEditObjet4 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_12)
        self.plainTextEditObjet4.setGeometry(QtCore.QRect(170, 150, 104, 31))
        self.plainTextEditObjet4.setObjectName("plainTextEditObjet4")
        self.plainTextEditObjet5 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_12)
        self.plainTextEditObjet5.setGeometry(QtCore.QRect(170, 180, 104, 31))
        self.plainTextEditObjet5.setObjectName("plainTextEditObjet5")
        self.plainTextEditObjet6 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_12)
        self.plainTextEditObjet6.setGeometry(QtCore.QRect(170, 210, 104, 31))
        self.plainTextEditObjet6.setObjectName("plainTextEditObjet6")
        self.plainTextEditObjet7 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_12)
        self.plainTextEditObjet7.setGeometry(QtCore.QRect(170, 240, 104, 31))
        self.plainTextEditObjet7.setObjectName("plainTextEditObjet7")
        self.plainTextEditObjet8 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_12)
        self.plainTextEditObjet8.setGeometry(QtCore.QRect(170, 270, 104, 31))
        self.plainTextEditObjet8.setObjectName("plainTextEditObjet8")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.label_15.setGeometry(QtCore.QRect(20, 40, 47, 13))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.label_16.setGeometry(QtCore.QRect(110, 40, 47, 13))
        self.label_16.setObjectName("label_16")
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.label_19.setGeometry(QtCore.QRect(190, 40, 47, 13))
        self.label_19.setObjectName("label_19")
        self.comboBoxObjet2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_12)
        self.comboBoxObjet2.setGeometry(QtCore.QRect(10, 100, 69, 22))
        self.comboBoxObjet2.setObjectName("comboBoxObjet2")
        self.comboBoxObjet2.addItem("")
        self.comboBoxObjet2.addItem("")
        self.comboBoxObjet2.addItem("")
        self.comboBoxObjet3 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_12)
        self.comboBoxObjet3.setGeometry(QtCore.QRect(10, 130, 69, 22))
        self.comboBoxObjet3.setObjectName("comboBoxObjet3")
        self.comboBoxObjet3.addItem("")
        self.comboBoxObjet3.addItem("")
        self.comboBoxObjet3.addItem("")
        self.comboBoxObjet4 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_12)
        self.comboBoxObjet4.setGeometry(QtCore.QRect(10, 160, 69, 22))
        self.comboBoxObjet4.setObjectName("comboBoxObjet4")
        self.comboBoxObjet4.addItem("")
        self.comboBoxObjet4.addItem("")
        self.comboBoxObjet4.addItem("")
        self.comboBoxObjet5 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_12)
        self.comboBoxObjet5.setGeometry(QtCore.QRect(10, 190, 69, 22))
        self.comboBoxObjet5.setObjectName("comboBoxObjet5")
        self.comboBoxObjet5.addItem("")
        self.comboBoxObjet5.addItem("")
        self.comboBoxObjet5.addItem("")
        self.comboBoxObjet6 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_12)
        self.comboBoxObjet6.setGeometry(QtCore.QRect(10, 220, 69, 22))
        self.comboBoxObjet6.setObjectName("comboBoxObjet6")
        self.comboBoxObjet6.addItem("")
        self.comboBoxObjet6.addItem("")
        self.comboBoxObjet6.addItem("")
        self.comboBoxObjet7 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_12)
        self.comboBoxObjet7.setGeometry(QtCore.QRect(10, 250, 69, 22))
        self.comboBoxObjet7.setObjectName("comboBoxObjet7")
        self.comboBoxObjet7.addItem("")
        self.comboBoxObjet7.addItem("")
        self.comboBoxObjet7.addItem("")
        self.comboBoxObjet8 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_12)
        self.comboBoxObjet8.setGeometry(QtCore.QRect(10, 280, 69, 22))
        self.comboBoxObjet8.setObjectName("comboBoxObjet8")
        self.comboBoxObjet8.addItem("")
        self.comboBoxObjet8.addItem("")
        self.comboBoxObjet8.addItem("")
        self.NumObjet2 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_12)
        self.NumObjet2.setGeometry(QtCore.QRect(100, 100, 61, 22))
        self.NumObjet2.setMaximum(8)
        self.NumObjet2.setObjectName("NumObjet2")
        self.NumObjet3 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_12)
        self.NumObjet3.setGeometry(QtCore.QRect(100, 130, 61, 22))
        self.NumObjet3.setMaximum(8)
        self.NumObjet3.setObjectName("NumObjet3")
        self.NumObjet4 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_12)
        self.NumObjet4.setGeometry(QtCore.QRect(100, 160, 61, 22))
        self.NumObjet4.setMaximum(8)
        self.NumObjet4.setObjectName("NumObjet4")
        self.NumObjet5 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_12)
        self.NumObjet5.setGeometry(QtCore.QRect(100, 190, 61, 22))
        self.NumObjet5.setMaximum(8)
        self.NumObjet5.setObjectName("NumObjet5")
        self.NumObjet6 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_12)
        self.NumObjet6.setGeometry(QtCore.QRect(100, 220, 61, 22))
        self.NumObjet6.setMaximum(8)
        self.NumObjet6.setObjectName("NumObjet6")
        self.NumObjet6_2 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_12)
        self.NumObjet6_2.setGeometry(QtCore.QRect(100, 250, 61, 22))
        self.NumObjet6_2.setMaximum(8)
        self.NumObjet6_2.setObjectName("NumObjet6_2")
        self.NumObjet8 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_12)
        self.NumObjet8.setGeometry(QtCore.QRect(100, 280, 61, 22))
        self.NumObjet8.setMaximum(8)
        self.NumObjet8.setObjectName("NumObjet8")
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_12)
        self.scrollArea_10 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_11)
        self.scrollArea_10.setGeometry(QtCore.QRect(400, 70, 171, 61))
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollArea_10.setObjectName("scrollArea_10")
        self.scrollAreaWidgetContents_15 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_15.setGeometry(QtCore.QRect(0, 0, 169, 59))
        self.scrollAreaWidgetContents_15.setObjectName("scrollAreaWidgetContents_15")
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents_15)
        self.label_17.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.label_17.setObjectName("label_17")
        self.NumBourse = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_15)
        self.NumBourse.setGeometry(QtCore.QRect(50, 30, 61, 22))
        self.NumBourse.setMaximum(50)
        self.NumBourse.setObjectName("NumBourse")
        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_15)
        self.ButtonSac = QtWidgets.QPushButton(self.scrollAreaWidgetContents_11)
        self.ButtonSac.setGeometry(QtCore.QRect(390, 180, 181, 61))
        self.ButtonSac.setObjectName("ButtonSac")
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_11)
        self.scrollArea_8 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_7)
        self.scrollArea_8.setGeometry(QtCore.QRect(0, 640, 101, 71))
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName("scrollArea_8")
        self.scrollAreaWidgetContents_13 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_13.setGeometry(QtCore.QRect(0, 0, 99, 69))
        self.scrollAreaWidgetContents_13.setObjectName("scrollAreaWidgetContents_13")
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents_13)
        self.label_20.setGeometry(QtCore.QRect(20, 10, 47, 13))
        self.label_20.setObjectName("label_20")
        self.plainTextEditHabilete = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_13)
        self.plainTextEditHabilete.setGeometry(QtCore.QRect(0, 30, 91, 31))
        self.plainTextEditHabilete.setObjectName("plainTextEditHabilete")
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_13)
        self.scrollArea_4 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_7)
        self.scrollArea_4.setGeometry(QtCore.QRect(190, 640, 351, 51))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 349, 49))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label_10.setObjectName("label_10")
        self.plainTextEditNom = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_9)
        self.plainTextEditNom.setGeometry(QtCore.QRect(70, 10, 151, 31))
        self.plainTextEditNom.setObjectName("plainTextEditNom")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_9)
        self.scrollArea_9 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_7)
        self.scrollArea_9.setGeometry(QtCore.QRect(100, 640, 91, 71))
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollArea_9.setObjectName("scrollArea_9")
        self.scrollAreaWidgetContents_14 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_14.setGeometry(QtCore.QRect(0, 0, 89, 69))
        self.scrollAreaWidgetContents_14.setObjectName("scrollAreaWidgetContents_14")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_14)
        self.label_21.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_21.setObjectName("label_21")
        self.plainTextEditEndurance = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_14)
        self.plainTextEditEndurance.setGeometry(QtCore.QRect(0, 30, 81, 31))
        self.plainTextEditEndurance.setObjectName("plainTextEditEndurance")
        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_14)
        self.ButtonFeuille = QtWidgets.QPushButton(self.scrollAreaWidgetContents_7)
        self.ButtonFeuille.setGeometry(QtCore.QRect(250, 710, 111, 41))
        self.ButtonFeuille.setObjectName("ButtonFeuille")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1125, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.buttonChapitre.clicked.connect(MainWindow.GoChapitre) # type: ignore
        self.chapitreNum.valueChanged['int'].connect(self.chapitreNum.selectAll) # type: ignore
        self.buttonProchainChapitre.clicked.connect(MainWindow.ProchainChapitre) # type: ignore
        self.ButtonArmes.clicked.connect(MainWindow.CreeArme) # type: ignore
        self.ButtonDiscipline.clicked.connect(MainWindow.CreeDiscipline) # type: ignore
        self.ButtonSac.clicked.connect(MainWindow.SacDos) # type: ignore
        self.ButtonFeuille.clicked.connect(MainWindow.FeuilleAventure) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonChapitre.setText(_translate("MainWindow", "GO"))
        self.label.setText(_translate("MainWindow", "Chapitre:"))
        self.buttonSauvegarde.setText(_translate("MainWindow", "sauvegarde"))
        self.label_4.setText(_translate("MainWindow", "Sauvegarde"))
        self.buttonLivre.setText(_translate("MainWindow", "GO"))
        self.label_5.setText(_translate("MainWindow", "Livre"))
        self.comboBoxLivre.setItemText(0, _translate("MainWindow", "Les Maitres des ténèbres 01"))
        self.buttonSuppSauvegarde.setText(_translate("MainWindow", "GO"))
        self.label_6.setText(_translate("MainWindow", "Supprimer sauvegarde"))
        self.label_8.setText(_translate("MainWindow", "Chapitre"))
        self.label_9.setText(_translate("MainWindow", "Se rendre au prochain chapitre"))
        self.buttonProchainChapitre.setText(_translate("MainWindow", "GO"))
        self.label_2.setText(_translate("MainWindow", "Création feuille d\'Aventure"))
        self.label_3.setText(_translate("MainWindow", "Discipline Kai"))
        self.ButtonDiscipline.setText(_translate("MainWindow", "Créer"))
        self.label_7.setText(_translate("MainWindow", "Notes"))
        self.label_11.setText(_translate("MainWindow", "Armes"))
        self.ButtonArmes.setText(_translate("MainWindow", "Créer"))
        self.label_12.setText(_translate("MainWindow", "Notes"))
        self.label_13.setText(_translate("MainWindow", "Sac A dos"))
        self.label_18.setText(_translate("MainWindow", "8 objet maximum repas comprit"))
        self.label_14.setText(_translate("MainWindow", "Objet"))
        self.comboBoxObjet1.setItemText(0, _translate("MainWindow", "Objet"))
        self.comboBoxObjet1.setItemText(1, _translate("MainWindow", "Repas"))
        self.comboBoxObjet1.setItemText(2, _translate("MainWindow", "Objet spéciaux"))
        self.label_15.setText(_translate("MainWindow", "Type"))
        self.label_16.setText(_translate("MainWindow", "Quantité"))
        self.label_19.setText(_translate("MainWindow", "Nom"))
        self.comboBoxObjet2.setItemText(0, _translate("MainWindow", "Objet"))
        self.comboBoxObjet2.setItemText(1, _translate("MainWindow", "Repas"))
        self.comboBoxObjet2.setItemText(2, _translate("MainWindow", "Objet spéciaux"))
        self.comboBoxObjet3.setItemText(0, _translate("MainWindow", "Objet"))
        self.comboBoxObjet3.setItemText(1, _translate("MainWindow", "Repas"))
        self.comboBoxObjet3.setItemText(2, _translate("MainWindow", "Objet spéciaux"))
        self.comboBoxObjet4.setItemText(0, _translate("MainWindow", "Objet"))
        self.comboBoxObjet4.setItemText(1, _translate("MainWindow", "Repas"))
        self.comboBoxObjet4.setItemText(2, _translate("MainWindow", "Objet spéciaux"))
        self.comboBoxObjet5.setItemText(0, _translate("MainWindow", "Objet"))
        self.comboBoxObjet5.setItemText(1, _translate("MainWindow", "Repas"))
        self.comboBoxObjet5.setItemText(2, _translate("MainWindow", "Objet spéciaux"))
        self.comboBoxObjet6.setItemText(0, _translate("MainWindow", "Objet"))
        self.comboBoxObjet6.setItemText(1, _translate("MainWindow", "Repas"))
        self.comboBoxObjet6.setItemText(2, _translate("MainWindow", "Objet spéciaux"))
        self.comboBoxObjet7.setItemText(0, _translate("MainWindow", "Objet"))
        self.comboBoxObjet7.setItemText(1, _translate("MainWindow", "Repas"))
        self.comboBoxObjet7.setItemText(2, _translate("MainWindow", "Objet spéciaux"))
        self.comboBoxObjet8.setItemText(0, _translate("MainWindow", "Objet"))
        self.comboBoxObjet8.setItemText(1, _translate("MainWindow", "Repas"))
        self.comboBoxObjet8.setItemText(2, _translate("MainWindow", "Objet spéciaux"))
        self.label_17.setText(_translate("MainWindow", "Bourse maximum 50 pièce d\'or"))
        self.ButtonSac.setText(_translate("MainWindow", "Ajouter"))
        self.label_20.setText(_translate("MainWindow", "Habileté"))
        self.label_10.setText(_translate("MainWindow", "Nom"))
        self.label_21.setText(_translate("MainWindow", "Endurance"))
        self.ButtonFeuille.setText(_translate("MainWindow", "Créer"))
