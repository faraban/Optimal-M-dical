SELECT * FROM Adresses

insert into Adresses
values (201, 1, 1),
	(4, 5, 6),
	(111, 1, 2),
	(173, 3, 5),
	(164, 4, 1),
	(23, 6, 9),
	(1, 1, 1),
	(12, 4, 5),
	(63, 11, 1),
	(24, 12, 3),
	(55, 9, 4),
	(16, 3, 6),
	(97, 1, 1),
	(18, 4, 5),
	(69, 11, 1),
	(201, 10, 3),
	(51, 11, 4),
	(4, 11, 2),
	(3, 6, 9),
	(20, 11, 3),
	(11, 8, 4),
	(5, 6, 1),
	(59, 11, 1),
	(121, 6, 1),
	(73, 3, 5),
	(164, 4,17),
	(118, 3, 6	);

SELECT * FROM Informations

insert into Informations
values ('HMA', '14366DG736', '4352617354', 1),
	('CHU', '73925TE792', '9302743892', 2),
	('CHR', '79375OZ027', '0373749292', 3),
	('PISAM', '84725JQ015', '9362719173', 5),
	('FARAH', '52896HS728', '5279286373', 4)

SELECT * FROM Users

insert into Users
values ('HMA', 'hma@gmail.com', '0000', 1),
	('CHU', 'chu@gmail.com', '0000', 2),
	('CHR', 'chr@gmail.com', '0000', 3),
	('PISAM', 'pisam@gmail.com', '0000', 4),
	('FARAH', 'farah@gmail.com', '0000', 5)

SELECT * FROM Services

insert into Services
values (10, 1, 1),
	(15, 1, 2),
	(12, 1, 3),
	(12, 1, 4),
	(8, 1, 5),
	(6, 4, 1),
	(5, 2, 2),
	(10, 8, 3),
	(7, 3, 4),
	(8, 5, 5)

SELECT * FROM Affiche

insert into Affiche
values (2, 'médecine générale', 4, 2, 1),
	(3, 'médecine générale', 6, 10, 2),
	(4, 'médecine générale', 3, 10, 3),
	(5, 'médecine générale', 7, 1, 4),
	(6, 'médecine générale', 3, 3, 5)


SELECT * FROM Reclamation

insert into Reclamation
values ('ma demande a pris du temps', 2),
	('veillez considérer ma demande svp',3),
	('accepter ma demande svp', 4),
	('ma demande sera acceptée quand ?', 5),
	('la suite de ma demande svp', 6)

SELECT * FROM Transfert

insert into Transfert
values ('2023-11-03 11:30:45', 1, 1, 2, 6),
	('2023-11-03 23:21:42', 1, 2, 3, 5),
	('2023-11-03 11:56:13', 1, 3, 4, 4),
	('2023-11-03 22:42:42', 1, 4, 5, 3),
	('2023-11-03 12:22:13', 1, 5, 6, 2)