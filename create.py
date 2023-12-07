# DSN = 'Driver={SQL Server};Server=DESKTOP-FRGCPSS\\SQLEXPRESS;Database=OptimalMedical;'
<<<<<<< HEAD
    
<<<<<<<
    

=======
# liste=['médecine générale','immunologie','radiologie','chirurgie','neurologie','pneumologie','cardiologie','odontologie','dermatologie','traumatologie','médecine interne','endocrinologie','anatomo-pathologie','hématologie','gastro-entérologie','urologie','pharmacie','maternité','Pédiatrie','Service des grands brûlés']
# conn = pyodbc.connect(DSN)
# cursor = conn.cursor()



# for user in liste:
#     cursor.execute('''INSERT INTO NomServices
#                     VALUES (?)
#                 ''', (user))
#     conn.commit()
>>>>>>> c4048d7af84e584dfb867bfabc68fbef26b51b22

# liste2=['stable','Rémission','Aggravation','Critique','Guérison','Chronique','Rémission','partielle','Rééducation']
# for user in liste2:
#     cursor.execute('''INSERT INTO EtatPatient
#                     VALUES (?)
#                 ''', (user))
#     conn.commit()


<<<<<<< HEAD
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
=======
# liste2=['stable','Rémission','Aggravation','Critique','Guérison','Chronique','Rémission','partielle','Rééducation']
>>>>>>> 40acb59e2b759155b3fdf47222c259e94d2d0c70
