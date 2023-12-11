CREATE DATABASE OptimalMedical

CREATE TABLE Adresses(
  IdAdresse INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  IdCommune INT NOT NULL,
  FOREIGN KEY (IdCommune) REFERENCES Commune(IdCommune),
  IdDepartement INT NOT NULL,
  FOREIGN KEY (IdDepartement) REFERENCES Departement(IdDepartement),
  IdRegion INT NOT NULL,
  FOREIGN KEY (IdRegion) REFERENCES Region(IdRegion),
  PositionGeo GEOGRAPHY NOT NULL
);

CREATE TABLE Commune(
  IdCommune INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  NomCommune VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Departement(
  IdDepartement INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  NomDepartement VARCHAR(50) NOT NULL UNIQUE
);
insert into Departement(ListeDepartement)
values
('Abidjan'),
('Agboville'),
('Aboisso'),
('Dabou'),
('Grand-Bassam'),
('Gagnoa'),
('Man'),
('Odienné'),
('Bouaké'),
('Yamoussoukro'),
('Bondoukou'),
('Korhogo');
select * from Departement

CREATE TABLE Region(
  IdRegion INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  NomRegion VARCHAR(50) NOT NULL UNIQUE
);

INSERT INTO Region(ListeRegion)
VALUES
  ('Gbôklé'),
  ('Nawa'),
  ('Indénié-Djuablin'),
  ('Sud-Comoé'),
  ('Folon'),
  ('Kabadougou'),
  ('Goh'),
  ('Lôh-Djiboua'),
  ('Bélier'),
  ('Iffou'),
  ('Moronou'),
  ('N’Zi'),
  ('Agnéby-Tiassa'),
  ('Grands-Ponts'),
  ('La Mé'),
  ('Cavally'),
  ('Guémon'),
  ('Tonkpi'),
  ('Haut-Sassandra'),
  ('Marahoué'),
  ('Bagoué'),
  ('Poro'),
  ('Tchologo'),
  ('Gbeke'),
  ('Hambol'),
  ('Béré'),
  ('Bafing'),
  ('Worodougou'),
  ('Bounkani'),
  ('Gontougo');

select * from Region

insert into Commune(ListeCommune)
values
('Agboville'),
('Akoupé'),
('Dabou'),
('Jacqueville'),
('Tiassalé'),
('Man'),
('Agboville'),
('Akoupé'),
('Dabou'),
('Jacqueville'),
('Tiassalé'),
('Boundiali'),
('Ferkessédougou'),
('Tengréla'),
('Kong'),
('Bouaké'),
('Sakassou'),
('Dabakala'),
('Béoumi'),
('Banfora'),
('Boromo'),
('Houndé'),
('Orodara'),
('Abengourou'),
('Abidjan'),
('Bonoua'),
('Grand-Bassam'),
('Tiassalé'),
('Dimbokro'),
('Bocanda'),
('M_Bahiakro'),
('Oumé'),
('Yamoussoukro'),
('Divo'),
('Tiébissou'),
('Taabo'),
('Daloa'),
('Issia'),
('Gagnoa'),
('Bouaké'),
('Béoumi'),
('Sakassou'),
('Dabakala'),
('Abengourou'),
('Bonoua'),
('Grand-Bassam'),
('Tiassalé');

select * from Commune

CREATE TABLE Informations(
  IdInformation INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  Nom VARCHAR(50) NOT NULL,
  Matricule VARCHAR(30) NOT NULL UNIQUE,
  Email VARCHAR(50) NOT NULL UNIQUE,
  Telephone INTEGER NOT NULL,
  IdAdresse INT NOT NULL,
  FOREIGN KEY (IdAdresse) REFERENCES Adresses(IdAdresse)
);
select * from Informations

CREATE TABLE Users(
  IdUser INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  NomUtilisateur VARCHAR(20) NOT NULL UNIQUE,
  Password VARCHAR(255) NOT NULL,
  IdInformation INT NOT NULL,
  FOREIGN KEY (IdInformation) REFERENCES Informations(IdInformation)
);

CREATE TABLE NomServices(
  IdNomServices INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  NomService VARCHAR(70) NOT NULL UNIQUE
);

CREATE TABLE Services(
  IdService INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  NombrePlace INTEGER NOT NULL,
  IdNomService INT NOT NULL,
  FOREIGN KEY (IdNomService) REFERENCES NomServices(IdNomServices),
  IdInformation INT NOT NULL,
  FOREIGN KEY (IdInformation) REFERENCES Informations(IdInformation)
);
--PROBLEME SUR LE TYPE BOOLEAN DE CETTE TABLE
--CREATE TABLE Affiche (
--  IdAffiche INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
--  Disponible BOOLEAN NOT NULL,
--  Attente BOOLEAN NOT NULL,
--  IdInformation INT NOT NULL,
--  FOREIGN KEY (IdInformation) REFERENCES Informations(IdInformation)
--);



CREATE TABLE Reclamation(
  IdReclamation INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  Commentaire VARCHAR(150) NOT NULL,
  IdInformation INT NOT NULL,
  FOREIGN KEY (IdInformation) REFERENCES Informations(IdInformation)
);

CREATE TABLE EtatPatient(
  IdEtatPatient INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  Etat VARCHAR(30) NOT NULL
);

CREATE TABLE Transfert(
  IdTransfert INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  IdService INT NOT NULL,
  FOREIGN KEY (IdService) REFERENCES Services(IdService),
  IdInformation INT NOT NULL,
  FOREIGN KEY (IdInformation) REFERENCES Informations(IdInformation)
  Etat VARCHAR(30) NOT NULL,
  FOREIGN KEY (Etat) REFERENCES EtatPatient(Etat)
  );

