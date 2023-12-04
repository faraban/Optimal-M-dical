import pyodbc
DSN = 'Driver={SQL Server};Server=DESKTOP-FRGCPSS\\SQLEXPRESS;Database=OptimalMedical;'
liste=['médecine générale','immunologie','radiologie','chirurgie','neurologie','pneumologie','cardiologie','odontologie','dermatologie','traumatologie','médecine interne','endocrinologie','anatomo-pathologie','hématologie','gastro-entérologie','urologie','pharmacie','maternité','Pédiatrie','Service des grands brûlés']
conn = pyodbc.connect(DSN)
cursor = conn.cursor()
# for user in liste:
#     cursor.execute('''INSERT INTO NomServices
#                     VALUES (?)
#                 ''', (user))
#     conn.commit()
    
# liste2=['stable','Rémission','Aggravation','Critique','Guérison','Chronique','Rémission','partielle','Rééducation']
# for user in liste2:
#     cursor.execute('''INSERT INTO EtatPatient
#                     VALUES (?)
#                 ''', (user))
#     conn.commit()