from flask import Flask, url_for, render_template, request, flash, redirect, abort, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


@app.route('/')
def Connexion():
    return render_template("./connexion/connexion.html")

#................brayane route (Inscription)#

@app.route('/inscriptioninfos')
def inscriptioninfos():
    return render_template("./inscription/inscriptioninfos.html")

@app.route('/inscriptionacces')
def inscriptionacces():
    return render_template("./inscription/inscriptionacces.html")

@app.route('/AjoutService')
def AjoutService():
    return render_template("./inscription/inscriptionservice0.html ")

#................Fin brayane route (Inscription)#


if __name__ == "__main__":
    app.run(debug=True)