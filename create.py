from flask import Flask, url_for, render_template, request, flash, redirect, abort, session
from werkzeug.security import generate_password_hash, check_password_hash
from sendcode import envoicode
import os
import requests
import random
import pyodbc
import pyodbc
DSN = 'Driver={SQL Server};Server=DESKTOP-FRGCPSS\\SQLEXPRESS;Database=OptimalMedical;' 


conn = pyodbc.connect(DSN)
cursor = conn.cursor()
cursor.execute("""
                SELECT Services.idservice, Services.Nombreplace, NomServices.NomService
                FROM services
                INNER JOIN NomServices ON NomServices.IdNomServices = Services.IdNomService
                WHERE IdInformation = ?
            """,4)
data = cursor.fetchall()
print(data)