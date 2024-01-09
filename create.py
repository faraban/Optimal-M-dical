from flask import Flask, url_for, render_template, request, flash, redirect, abort, session
import pyodbc
DSN = 'Driver={SQL Server};Server=DESKTOP-FRGCPSS\\SQLEXPRESS;Database=OptimalMedical;' 

idinformation=2
conn = pyodbc.connect(DSN)
cursor = conn.cursor()
# cursor.execute(''' 
#             SELECT InfoDep.Nom, InfoDes.Nom, NomServices.NomService, EtatPatient.Etat, Transfert.Dateheure
#             FROM Transfert 
#             INNER JOIN Users AS UsersDep ON Transfert.IdUserDep = UsersDep.IdUser
#             INNER JOIN Users AS UsersDes ON Transfert.IdUserDes = UsersDes.IdUser
#             INNER JOIN Informations AS InfoDep ON UsersDep.IdInformation = InfoDep.IdInformation
#             INNER JOIN Informations AS InfoDes ON UsersDes.IdInformation = InfoDes.IdInformation
#             INNER JOIN NomServices ON Transfert.IdNomService = NomServices.IdNomService
#             INNER JOIN EtatPatient ON Transfert.IdEtatPatient = EtatPatient.IdEtatPatient
#         ''')
# services = cursor.fetchone()
cursor.execute('''
            SELECT transfert.dateheure, InfoDes.Nom, NomServices.NomService , etatpatient.etat, Departement.NomDepartement, Commune.NomCommune
            FROM transfert
            INNER JOIN NomServices ON NomServices.IdNomServices = transfert.IdNomService
            INNER JOIN etatpatient ON etatpatient.Idetatpatient = transfert.Idetatpatient
            INNER JOIN Users AS UsersDes ON Transfert.IdUserDes = UsersDes.IdUser
            INNER JOIN Informations AS InfoDes ON UsersDes.IdInformation = InfoDes.IdInformation
            INNER JOIN Adresses ON Adresses.IdAdresse = InfoDes.IdAdresse
            INNER JOIN Departement ON Departement.IdDepartement = Adresses.IdDepartement
            INNER JOIN Commune ON Adresses.IdCommune = Commune.IdCommune
            where transfert.Iduserdep = ?
            ''', 1)
data = cursor.fetchall()
print(data)