import pyodbc
DSN = 'Driver={SQL Server};Server=DESKTOP-FRGCPSS\\SQLEXPRESS;Database=OptimalMedical;' 

Commune=2
departement=11
region=21
conn = pyodbc.connect(DSN)
cursor = conn.cursor()
cursor.execute('''insert into Adresses (idCommune, idDepartement,idRegion) values(?,?,?)''',(Commune,departement,region))
conn.commit() 
conn.close()