import pyodbc
DSN = 'Driver={SQL Server};Server=DESKTOP-FRGCPSS\\SQLEXPRESS;Database=OptimalMedical;' 


conn = pyodbc.connect(DSN)
cursor = conn.cursor()

cursor.execute('''
SELECT * FROM Nomservices 
''')
service= cursor.fetchall()
print(service)