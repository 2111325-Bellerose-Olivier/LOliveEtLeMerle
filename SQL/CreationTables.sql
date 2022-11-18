CREATE DATABASE IF NOT EXISTS merlive;
USE merlive;

CREATE TABLE IF NOT EXISTS feuille_aventure(
	id INT PRIMARY KEY AUTO_INCREMENT,
	endurance INT,
	habilite VARCHAR(255),
	bourse INT
);


CREATE TABLE IF NOT EXISTS discipline_kai(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nom VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS arme(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nom VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS objet(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nom VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS lien_discipline_kai(
id INT PRIMARY KEY AUTO_INCREMENT,
id_feuille_aventure INT,
id_discipline_kai INT,
FOREIGN KEY (id_discipline_kai) REFERENCES discipline_kai(id),
FOREIGN KEY (id_feuille_aventure) REFERENCES feuille_aventure(id)
);

CREATE TABLE IF NOT EXISTS lien_arme(
id INT PRIMARY KEY AUTO_INCREMENT,
id_feuille_aventure INT,
id_arme INT,
FOREIGN KEY (id_arme) REFERENCES arme(id),
FOREIGN KEY (id_feuille_aventure) REFERENCES feuille_aventure(id)
);

CREATE TABLE IF NOT EXISTS lien_objet(
id INT PRIMARY KEY AUTO_INCREMENT,
id_feuille_aventure INT,
id_objet iNT,
FOREIGN KEY (id_objet) REFERENCES objet(id),
FOREIGN KEY (id_feuille_aventure) REFERENCES feuille_aventure(id)
);


CREATE TABLE IF NOT EXISTS chapitre(
	id INT PRIMARY KEY AUTO_INCREMENT,
	no_chapitre INT,
	texte VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS lien_chapitre(
	id INT PRIMARY KEY AUTO_INCREMENT,
	no_chapitre_origine INT,
	no_chapitre_destination INT,
	FOREIGN KEY (no_chapitre_origine) REFERENCES chapitre(id),
	FOREIGN KEY (no_chapitre_destination) REFERENCES chapitre(id)
);

CREATE TABLE IF NOT EXISTS sauvegarde(
id INT PRIMARY KEY AUTO_INCREMENT,
no_chapitre INT,
feuille_aventure INT,
FOREIGN KEY (no_chapitre) REFERENCES chapitre(id),
FOREIGN KEY (feuille_aventure) REFERENCES feuille_aventure(id)
);