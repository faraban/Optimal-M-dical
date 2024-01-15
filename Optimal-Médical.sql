CREATE DATABASE OptimalMedical;

CREATE TABLE Commune(
  IdCommune INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  NomCommune VARCHAR(50) NOT NULL UNIQUE
);

<<<<<<< Updated upstream
=======
select * from Commune
>>>>>>> Stashed changes
CREATE TABLE Departement(
  IdDepartement INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  NomDepartement VARCHAR(50) NOT NULL UNIQUE
);

select * from Departement

CREATE TABLE Region(
  IdRegion INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  NomRegion VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Adresses(
  IdAdresse INT PRIMARY KEY NOT NULL,
  IdCommune INT NOT NULL,
  FOREIGN KEY (IdCommune) REFERENCES Commune(IdCommune),
  IdDepartement INT NOT NULL,
  FOREIGN KEY (IdDepartement) REFERENCES Departement(IdDepartement),
  IdRegion INT NOT NULL,
  FOREIGN KEY (IdRegion) REFERENCES Region(IdRegion),
  positiongeo varchar(100) not null
);

	insert into Departement
	values  ('Abidjan'),
		('Agboville'),
		('Sikensi'),
		('Taabo'),
		('Tiassalé'),
		('Koro'),
		('Ouaninou'),
		('Touba'),
		('Boundiali'),
		('Kouto'),
		('Tengrela'),
		('Didievi'),
		('Djékanou'),
		('Tiebissou'),
		('Toumodi'),
		('Dianra'),
		('Kounahiri'),
		('Mankono'),
		('Bouna'),
		('Doropo'),
		('Nassian'),
		('Tehini'),
		('Blolequin'),
		('Guiglo'),
		('Tai'),
		('Toulepleu');

INSERT INTO Region
VALUES
  ('District autonome Abidjan'),
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
  ('Gontougo'),
  ('San-Pédro'),
  ('District autonome de Yamoussoukro');

insert into Commune
values ('Abengourou'),
		('Abobo'),
		('Aboisso'),
		('Adiake'),
		('Adjame'),
		 ('Adzope'),
		 ('Affery'),
		 ('Agboville'),
		 ('Agnibilekro'),
		 ('Agou'),
		('Akoupe'),
		('Alepe'),
		('Anoumaba'),
		('Anyama'),
		('Arrah'),
		('Assinie mafia'),
		('Assuefry'),
		('Attecoube'),
		('Attiegouakro'),
		('Ayame'),
		('Azaguie'),
		('Bako'),
		('Bangolo'),
		('Bassawa'),
		('Bediala'),
		('Beoumi'),
		('Bettie'),
		('Biankouma'),
		('Bingerville'),
		('Binhouye'),
		('Blolequin'),
		('Bocanda'),
		('Bodokro'),
		('Bondoukou'),
		('Bongouanou'),
		('Bonieredougou'),
		('Bonon'),
		('Bonoua'),
		('Booko'),
		('Borotou'),
		('Botro'),
		('Bouafle'),
		('Bouake'),
		('Bouna'),
		('Boundiali'),
		('Brobo'),
		('Buyo'),
		('Cocody'),
		('Dabakala'),
		('Dabou'),
		('Daloa'),
		('Danane'),
		('Daoukro'),
		('Diabo'),
		('Dianra'),
		('Diawala'),
		('Didievi'),
		('Diegonefla'),
		('Dikodougou'),
		('Dimbokro'),
		('Dioulatiedougou'),
		('Divo'),
		('Djebonoua'),
		('Djekanou'),
		('Djibrosso'),
		('Doropo'),
		('Dualla'),
		('Duekoue'),
		('Ettrokro'),
		('Facobly'),
		('Ferkessedougou'),
		('Foumbolo'),
		('Fresco'),
		('Fronan'),
		('Gagnoa'),
		('Gbeleban'),
		('Gboguhe'),
		('Gbon'),
		('Gbonne'),
		('Gohitafla'),
		('Goulia'),
		('Grabo'),
		('Grand bassam'),
		('Grand bereby'),
		('Grand lahou'),
		('Grand zattry'),
		('Gueyo'),
		('Guiberoua'),
		('Guiembre'),
		('Guiglo'),
		('Guinteguela'),
		('Guitry'),
		('Hire'),
		('Issia'),
		('Jacqueville'),
		('Kanakono'),
		('Kani'),
		('Kaniasso'),
		('Karakoro'),
		('Kassere'),
		('Katiola'),
		('Kokoumbo'),
		('Kolia'),
		('Komborodougou'),
		('Kong'),
		('Kongasso'),
		('Koonan'),
		('Korhogo'),
		('Koro'),
		('Kouassi dattekro'),
		('Kouassi kouassikro'),
		('Kouibly'),
		('Koumassi'),
		('Koumbala'),
		('Koun fao'),
		('Kounahiri'),
		('Kouto'),
		('Lakota'),
		('Logouale'),
		('Mbahiakro'),
		('Mbatto'),
		('Mbengue'),
		('Madinani'),
		('Mafere'),
		('Man'),
		('Mankono'),
		('Marcory'),
		('Massala'),
		('Mayo'),
		('Meagui'),
		('Minignan'),
		('Morondo'),
		('Ndouci'),
		('Napie'),
		('Nassian'),
		('Niable'),
		('Niakaramadougou'),
		('Nielle'),
		('Niofoin'),
		('Odienne'),
		('Ouangolodougou'),
		('Ouaninou'),
		('Ouelle'),
		('Oume'),
		('Ouragahio'),
		('Plateau'),
		('Port bouet'),
		('Prikro'),
		('Rubino'),
		('Saioua'),
		('Sakassou'),
		('Samatiguila'),
		('San pedro'),
		('Sandegue'),
		('Sangouine'),
		('Sarhala'),
		('Sassandra'),
		('Satama sokoro'),
		('Satama sokoura'),
		('Seguela'),
		('Seguelon'),
		('Seydougou'),
		('Sifie'),
		('Sikensi'),
		('Sinematiali'),
		('Sinfra'),
		('Sipilou'),
		('Sirasso'),
		('Songon'),
		('Soubre'),
		('Taabo'),
		('Tabou'),
		('Tafire'),
		('Tai'),
		('Tanda'),
		('Tehini'),
		('Tengrela'),
		('Tiapoum'),
		('Tiassale'),
		('Tie ndiekro'),
		('Tiebissou'),
		('Tieme'),
		('Tiemelekro'),
		('Tieningboue'),
		('Tienko'),
		('Tioroniaradougou'),
		('Tortiya'),
		('Touba'),
		('Toulepleu'),
		('Toumodi'),
		('Transua'),
		('Treichville'),
		('Vavoua'),
		('Worofla'),
		('Yakasse attobrou'),
		('Yamoussoukro'),
		('Yopougon'),
		('Zikisso')	,
		('Zouan hounien'),
		('Zoukougbeu'),
		('Zuenoula');


CREATE TABLE Informations(
  IdInformation INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  Nom VARCHAR(50) NOT NULL,
  Matricule VARCHAR(30) NOT NULL UNIQUE,
  Telephone VARCHAR(15) NOT NULL,
  IdAdresse INT NOT NULL,
  FOREIGN KEY (IdAdresse) REFERENCES Adresses(IdAdresse),
  lienimg varchar(100)
);


CREATE TABLE Users(
  IdUser INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  NomUtilisateur VARCHAR(20) NOT NULL UNIQUE,
  email VARCHAR(100) NOT NULL UNIQUE,
  Password VARCHAR(255) NOT NULL,
  IdInformation INT NOT NULL,
  FOREIGN KEY (IdInformation) REFERENCES Informations(IdInformation),
  categorie varchar(10) not null
);

CREATE TABLE NomServices(
  IdNomServices INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  NomService VARCHAR(70) NOT NULL UNIQUE
);

INSERT INTO NomServices
VALUES ('Médecine générale'),
        ('Pédiatrie'),
        ('Gynécologie-obstétrique'),
        ('Gériatrie'),
		('Cardiologie'),
		('Neurologie'),
		('Pneumologie'),
		('Gastro-entérologie'),
		('Hépatologie'),
		('Endocrinologie'),
		('Rhumatologie'),
		('Dermatologie'),
		('Ophtalmologie'),
		('Oto-rhino-laryngologie'),
		('Urologie'),
		('Chirurgie générale'),
		('Chirurgie'),
		('Chirurgie pédiatrique'),
		('Anesthésie'),
		('Réanimation'),
		('Urgence'),
		('Psychiatrie'),
		('Médecine du travail'),
		('Kinésithérapie'),
		('Diététique'),
		('Rééducation'),
        ('Service des grands brûlés');

CREATE TABLE Services(
  IdService INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  NombrePlace INTEGER NOT NULL,
  PlaceDisponible INTEGER NOT NULL,
  Attente INTEGER NOT NULL,
  IdNomService INT NOT NULL,
  FOREIGN KEY (IdNomService) REFERENCES NomServices(IdNomServices),
  IdInformation INT NOT NULL,
  FOREIGN KEY (IdInformation) REFERENCES Informations(IdInformation)
);

CREATE TABLE Affiche (
	IdAffiche INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
	iduser int not null,
	service varchar(70) not null,
	Disponible int NOT NULL,
	Attente int NOT NULL,
	IdInformation INT NOT NULL,
	FOREIGN KEY (Iduser) REFERENCES users(Iduser),
	FOREIGN KEY (IdInformation) REFERENCES Informations(IdInformation)
);

CREATE TABLE Reclamation(
  IdReclamation INT primary KEY IDENTITY(1, 1) NOT NULL,
  Commentaire VARCHAR(150) NOT NULL,
  Iduser INT NOT NULL,
  FOREIGN KEY (Iduser) REFERENCES users(Iduser)
);

CREATE TABLE EtatPatient(
  IdEtatPatient INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  Etat VARCHAR(30) NOT NULL
);

INSERT INTO EtatPatient
VALUES ('Stable'),
       ('Rémission'),
       ('Aggravation'),
       ('Critique'),
       ('Guérison'),
       ('Chronique'),
       ('Rémission'),
       ('Partielle'),
       ('Rééducation');

CREATE TABLE Transfert(
  IdTransfert INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  IdUserDep INT NOT NULL,
  FOREIGN KEY (IdUserDep) REFERENCES users(Iduser),
  IdUserDes INT NOT NULL,
  FOREIGN KEY (IdUserDes) REFERENCES users(Iduser),
  IdNomService INT NOT NULL,
  FOREIGN KEY (IdNomService) REFERENCES NomServices(IdNomServices),
  IdEtatPatient INT NOT NULL,
  FOREIGN KEY (IdEtatPatient) REFERENCES EtatPatient(IdEtatPatient),
  Dateheure DATETIME NOT NULL
  );


  select * from Users
  select * from transfert

  SELECT InfoDep.Nom, InfoDes.Nom, NomServices.NomService, EtatPatient.Etat, Transfert.Temps
                FROM Transfert 
                INNER JOIN Users AS UsersDep ON Transfert.IdUserDep = UsersDep.IdUser
                INNER JOIN Users AS UsersDes ON Transfert.IdUserDes = UsersDes.IdUser
                INNER JOIN Informations AS InfoDep ON UsersDep.IdInformation = InfoDep.IdInformation
                INNER JOIN Informations AS InfoDes ON UsersDes.IdInformation = InfoDes.IdInformation
                INNER JOIN Services ON Transfert.IdService = Services.IdService
                INNER JOIN NomServices ON NomServices.IdNomServices = Services.IdNomService
                INNER JOIN EtatPatient ON Transfert.IdEtatPatient = EtatPatient.IdEtatPatient