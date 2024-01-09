from flask import Flask, url_for, render_template, request, flash, redirect, abort, session
import pyodbc
DSN = 'Driver={SQL Server};Server=DESKTOP-FRGCPSS\\SQLEXPRESS;Database=OptimalMedical;' 

idinformation=2
conn = pyodbc.connect(DSN)
cursor = conn.cursor()
# cursor.execute("""
#             SELECT Informations.Matricule, Informations.Nom, Users.email, Commune.NomCommune, Departement.NomDepartement
#             , Region.NomRegion, Informations.Telephone
#             FROM Informations, Users, Adresses, Commune, Departement, Region
#             WHERE Informations.IdInformation = Users.IdInformation 
#             AND Informations.IdAdresse = Adresses.IdAdresse
#             AND Adresses.IdCommune = Commune.IdCommune
#             AND Adresses.IdDepartement = Departement.IdDepartement
#             AND Adresses.IdRegion = Region.IdRegion
#         """)
# data = cursor.fetchall()

cursor.execute('''
                SELECT Services.idservice, Informations.Nom,Services.Nombreplace, NomServices.NomService, Services.placedisponible, Services.attente
                FROM services
                INNER JOIN NomServices ON NomServices.IdNomServices = Services.IdNomService
                INNER JOIN Informations ON Informations.IdInformation = Services.IdInformation
                where services.IdInformation != ?
                ''',idinformation)
data = cursor.fetchall()