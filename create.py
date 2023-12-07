# DSN = 'Driver={SQL Server};Server=DESKTOP-FRGCPSS\\SQLEXPRESS;Database=OptimalMedical;'
    
<<<<<<<
    


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
