# DSN = 'Driver={SQL Server};Server=DESKTOP-FRGCPSS\\SQLEXPRESS;Database=OptimalMedical;'
    
<<<<<<<
    


# liste2=['stable','Rémission','Aggravation','Critique','Guérison','Chronique','Rémission','partielle','Rééducation']
# for user in liste2:
#     cursor.execute('''INSERT INTO EtatPatient
#                     VALUES (?)
#                 ''', (user))
#     conn.commit()


liste2=['stable','Rémission','Aggravation','Critique','Guérison','Chronique','Rémission','partielle','Rééducation']
for user in liste2:
    print(user)
=======
liste2=['stable','Rémission','Aggravation','Critique','Guérison','Chronique','Rémission','partielle','Rééducation']
for user in liste2:
    cursor.execute('''INSERT INTO EtatPatient
                    VALUES (?)
                 ''', (user))
    conn.commit()
>>>>>>>