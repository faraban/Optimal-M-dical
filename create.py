from flask import Flask, url_for, render_template, request, flash, redirect, abort, session
import pyodbc
DSN = 'Driver={SQL Server};Server=DESKTOP-FRGCPSS\\SQLEXPRESS;Database=OptimalMedical;' 

idinformation=2
conn = pyodbc.connect(DSN)
cursor = conn.cursor()
cursor.execute("UPDATE services SET placedisponible = ? WHERE idservice = ?", (10, 5))
conn.commit()
