from flask import Flask, url_for, render_template, request, flash, redirect, abort, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


@app.route('/')
def Connexion():
    return render_template("./connexion/connexion.html")

@app.route('/inscriptionacces')
def inscription1():
    return render_template("./inscription/inscriptionacces.html")

if __name__ == "__main__":
    app.run(debug=True)