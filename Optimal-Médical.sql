CREATE DATABASE OptimalMedical

CREATE TABLE Adresses(
IdAdresse INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
Commune VARCHAR(50) NOT NULL,
Departement VARCHAR(50) NOT NULL,
Region VARCHAR(50) NOT NULL,
PositionGeo GEOGRAPHY NOT NULL
);

CREATE TABLE Informations(
IdInformation  INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
Nom VARCHAR(50) NOT NULL,
Matricule VARCHAR(30) NOT NULL,
Email VARCHAR(50) NOT NULL,
Telephone VARCHAR(15) NOT NULL,
IdAdresse INT,
FOREIGN KEY (IdAdresse) REFERENCES Adresses(IdAdresse)
);

CREATE TABLE Users(
IdUser INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
NomUtilisateur VARCHAR(20) NOT NULL,
Password VARCHAR(255) NOT NULL,
IdInformation INT,
FOREIGN KEY (IdInformation) REFERENCES Informations(IdInformation)
);

CREATE TABLE NomServices(
IdNomServices INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
NomService VARCHAR(70) NOT NULL
);

CREATE TABLE Services(
IdService INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
NombrePlace VARCHAR(50) NOT NULL,
IdNomService INT,
FOREIGN KEY (IdNomService) REFERENCES NomServices(IdNomServices),
IdInformation INT,
FOREIGN KEY (IdInformation) REFERENCES Informations(IdInformation)
);

CREATE TABLE Affiche (
IdAffiche INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
Disponible INT NOT NULL,
Attente INT NOT NULL,
IdInformation INT,
FOREIGN KEY (IdInformation) REFERENCES Informations(IdInformation)
);
CREATE TABLE Reclamation(
IdReclamation INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
commentaire VARCHAR(150),
IdInformation INT,
FOREIGN KEY (IdInformation) REFERENCES Informations(IdInformation)
);

CREATE TABLE EtatPatient(
IdEtatPatient INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
Etat VARCHAR(30)
);

CREATE TABLE Transfert(
IdTransfert INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
IdService INT,
FOREIGN KEY (IdService) REFERENCES Services(IdService),
IdInformation INT,
FOREIGN KEY (IdInformation) REFERENCES Informations(IdInformation),
IdEtatPatient INT,
FOREIGN KEY (IdEtatPatient) REFERENCES EtatPatient(IdEtatPatient)
);

