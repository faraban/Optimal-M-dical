from flask import Flask, url_for, render_template, request, flash, redirect, abort, session
import pyodbc
DSN = 'Driver={SQL Server};Server=DESKTOP-FRGCPSS\\SQLEXPRESS;Database=OptimalMedical;' 


conn = pyodbc.connect(DSN)
cursor = conn.cursor()

cursor.execute(''' SELECT * FROM services 
        where idService= ?
        ''',4)
services = cursor.fetchone()
print(services)