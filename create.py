from flask import Flask, url_for, render_template, request, flash, redirect, abort, session
import pyodbc
DSN = 'Driver={SQL Server};Server=DESKTOP-FRGCPSS\\SQLEXPRESS;Database=OptimalMedical;' 

idinformation=2
conn = pyodbc.connect(DSN)
cursor = conn.cursor()
cursor.execute(''' SELECT * FROM services 
        where idService= ?
        ''',5)
services = cursor.fetchone()
if services[2]>services[3]:
        cursor.execute('''
                       UPDATE services 
                       SET PlaceDisponible =5  
                       WHERE IdService = ?
                       ''',2)
        print(services)