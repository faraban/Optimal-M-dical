CREATE DATABASE OptimalMedical;

CREATE TABLE Commune(
  IdCommune INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  NomCommune VARCHAR(50) NOT NULL UNIQUE
);


CREATE TABLE Departement(
  IdDepartement INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  NomDepartement VARCHAR(50) NOT NULL UNIQUE
);

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

INSERT INTO Region
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

insert into Commune
values ('abengourou'),
		('abobo'),
		('aboisso'),
		('adiake'),
		('adjame'),
		 ('adzope'),
		 ('affery'),
		 ('agboville'),
		 ('agnibilekro'),
		 ('agou'),
		('akoupe'),
		('alepe'),
		('anoumaba'),
		('anyama'),
		('arrah'),
		('assinie mafia'),
		('assuefry'),
		('attecoube'),
		('attiegouakro'),
		('ayame'),
		('azaguie'),
		('bako'),
		('bangolo'),
		('bassawa'),
		('bediala'),
		 ('beoumi'),
		 ('bettie'),
		 ('biankouma'),
		 ('bingerville'),
		 ('binhouye'),
		('blolequin'),
		('bocanda'),
		('bodokro'),
		('bondoukou'),
		('bongouanou'),
		('bonieredougou'),
		('bonon'),
		('bonoua'),
		('booko'),
		('borotou'),
		('botro'),
		('bouafle'),
		('bouake'),
		('bouna'),
		('boundiali'),
		('brobo'),
		('buyo'),
		('cocody'),
		('dabakala'),
		('dabou'),
		('daloa'),
		('danane'),
		('daoukro'),
		('diabo'),
		('dianra'),
		('diawala'),
		('didievi'),
		('diegonefla'),
		('dikodougou'),
		('dimbokro'),
		 ('dioulatiedougou'),
		 ('divo'),
		 ('djebonoua'),
		 ('djekanou'),
		 ('djibrosso'),
		('doropo'),
		('dualla'),
		('duekoue'),
		('ettrokro'),
		('facobly'),
		('ferkessedougou'),
		('foumbolo'),
		('fresco'),
		('fronan'),
		('gagnoa'),
		('gbeleban'),
		('gboguhe'),
		('gbon'),
		('gbonne'),
		('gohitafla'),
		('goulia'),
		('grabo'),
		('grand bassam'),
		('grand bereby'),
		('grand lahou'),
		('grand zattry'),
		('gueyo'),
		('guiberoua'),
		('guiembre'),
		('guiglo'),
		('guinteguela'),
		('guitry'),
		('hire'),
		('issia'),
		('jacqueville'),
		('kanakono'),
		('kani'),
		('kaniasso'),
		('karakoro'),
		('kassere'),
		('katiola'),
		('kokoumbo'),
		('kolia'),
		('komborodougou'),
		('kong'),
		('kongasso'),
		('koonan'),
		('korhogo'),
		('koro'),
		('kouassi dattekro'),
		('kouassi kouassikro'),
		('kouibly'),
		('koumassi'),
		('koumbala'),
		('koun fao'),
		('kounahiri'),
		('kouto'),
		('lakota'),
		('logouale'),
		('mbahiakro'),
		('mbatto'),
		('mbengue'),
		('madinani'),
		('mafere'),
		('man'),
		('mankono'),
		('marcory'),
		('massala'),
		('mayo'),
		('meagui'),
		('minignan'),
		('morondo'),
		('ndouci'),
		('napie'),
		('nassian'),
		('niable'),
		('niakaramadougou'),
		('nielle'),
		('niofoin'),
		('odienne'),
		('ouangolodougou'),
		('ouaninou'),
		('ouelle'),
		('oume'),
		('ouragahio'),
		('plateau'),
		('port bouet'),
		('prikro'),
		('rubino'),
		('saioua'),
		('sakassou'),
		('samatiguila'),
		('san pedro'),
		('sandegue'),
		('sangouine'),
		('sarhala'),
		('sassandra'),
		('satama sokoro'),
		('satama sokoura'),
		('seguela'),
		('seguelon'),
		('seydougou'),
		('sifie'),
		('sikensi'),
		('sinematiali'),
		('sinfra'),
		('sipilou'),
		('sirasso'),
		('songon'),
		('soubre'),
		('taabo'),
		('tabou'),
		('tafire'),
		('tai'),
		('tanda'),
		('tehini'),
		('tengrela'),
		('tiapoum'),
		('tiassale'),
		('tie ndiekro'),
		('tiebissou'),
		('tieme'),
		('tiemelekro'),
		('tieningboue'),
		('tienko'),
		('tioroniaradougou'),
		('tortiya'),
		('touba'),
		('toulepleu'),
		('toumodi'),
		('transua'),
		('treichville'),
		('vavoua'),
		('worofla'),
		('yakasse attobrou'),
		('yamoussoukro'),
		('yopougon'),
		('zikisso')	,
		('zouan hounien'),
		('zoukougbeu'),
		( 'zuenoula');

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
VALUES ('médecine générale'),
        ('immunologie'),
        ('radiologie'),
        ('chirurgie'),
        ('neurologie'),
        ('pneumologie'),
        ('cardiologie'),
        ('odontologie'),
        ('dermatologie'),
        ('traumatologie'),
        ('médecine interne'),
        ('endocrinologie'),
        ('anatomo-pathologie'),
        ('hématologie'),
        ('gastro-entérologie'),
        ('urologie'),
        ('pharmacie'),
        ('maternité'),
        ('Pédiatrie'),
        ('Service des grands brûlés');

CREATE TABLE Services(
  IdService INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  NombrePlace INTEGER NOT NULL,
  placedisponible INTEGER NOT NULL,
  attente INTEGER NOT NULL,
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
  IdReclamation INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  Commentaire VARCHAR(150) NOT NULL,
  Iduser INT NOT NULL,
  FOREIGN KEY (Iduser) REFERENCES users(Iduser)
);

CREATE TABLE EtatPatient(
  IdEtatPatient INT PRIMARY KEY IDENTITY(1, 1) NOT NULL,
  Etat VARCHAR(30) NOT NULL
);

INSERT INTO EtatPatient
VALUES ('stable'),
        ('Rémission'),
        ('Aggravation'),
        ('Critique'),
        ('Guérison'),
        ('Chronique'),
        ('Rémission'),
        ('partielle'),
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


UPDATE Users
SET categorie = 'OK'
FROM Users
INNER JOIN Informations ON Users.IdInformation=Informations.IdInformation
WHERE NomUtilisateur = 'admin'