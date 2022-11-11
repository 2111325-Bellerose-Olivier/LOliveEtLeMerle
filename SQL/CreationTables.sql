CREATE TABLE discipline_kai(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nom VARCHAR(255),
	notes VARCHAR(255)
);

CREATE TABLE arme(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nom VARCHAR(255),
	notes VARCHAR(255)
);

CREATE TABLE sac_dos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	type_objet ENUM('objet','objet_special','bourse','repas'),
	nombre_objet INT,
	nom_objet VARCHAR(255),
	notes_bas VARCHAR(255)
);

CREATE TABLE feuille_aventure(
	id INT PRIMARY KEY AUTO_INCREMENT,
	id_discipline_kai INT,
	id_arme INT,
	endurance INT,
	habilite VARCHAR(255),
	id_sac_dos INT,
	FOREIGN KEY (id_discipline_kai) REFERENCES discipline_kai(id),
	FOREIGN KEY (id_arme) REFERENCES arme(id),
	FOREIGN KEY (id_sac_dos) REFERENCES sac_dos(id)
);

CREATE TABLE chapitre(
	id INT PRIMARY KEY AUTO_INCREMENT,
	no_chapitre INT,
	texte VARCHAR(255)
);

CREATE TABLE lien_chapitre(
	id INT PRIMARY KEY AUTO_INCREMENT,
	no_chapitre_origine INT,
	no_chapitre_destination INT,
	FOREIGN KEY (no_chapitre_origine) REFERENCES chapitre(id),
	FOREIGN KEY (no_chapitre_destination) REFERENCES chapitre(id)
);