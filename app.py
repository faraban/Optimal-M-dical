from flask import Flask, url_for, render_template, request, flash, redirect, abort, session
from werkzeug.security import generate_password_hash, check_password_hash
import pyodbc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clés_flash'
DSN = 'Driver={SQL Server};Server=DESKTOP-FRGCPSS\SQLEXPRESS;Database=OptimalMedical;'


#  utilisateurs


@app.route('/monhopital')
def monhopital():
    value=['stable','Rémission','Aggravation','Critique','Guérison','Chronique','Rémission','partielle','Rééducation']
    return render_template("./utilisateur/utilisateurhôpital.html",value=value)


@app.route('/monprofil')
def monprofil():
    return render_template("./utilisateur/utilisateurprofil.html")


@app.route('/transfert')
def transfert():
    value=['stable','Rémission','Aggravation','Critique','Guérison','Chronique','Rémission','partielle','Rééducation']
    return render_template("./utilisateur/utilisateurtransfert.html",value=value)


# ................brayane route (Inscription)#

@app.route('/inscriptioninfos')
def inscriptioninfos():
    return render_template("./inscription/inscriptioninfos.html")


@app.route('/inscriptionacces')
def inscriptionacces():
    data = ''
    return render_template("./inscription/inscriptionacces.html", data=data)


@app.route('/ListeService')
def listeservice():
    return render_template("./inscription/inscriptionservice.html ")


@app.route('/AjoutService')
def ajoutservice():
    return render_template("./inscription/inscriptionservice0.html ")


# ................Fin brayane route (Inscription)#
#     connexion 

@app.route("/", methods=["GET", "POST"])
def accueil():
    if 'loggedin' in session:
        return render_template("/connexion/accueil.html", username=session['username'], title="accueil")
    return redirect(url_for('connexion'))


@app.route("/connexion", methods=["GET", "POST"])
def connexion():
    if request.method == 'POST':
        user = request.form["identifiant"]
        password = request.form["password"]
        conn = pyodbc.connect(DSN)
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM Users 
        INNER JOIN Informations ON Informations.IdInformation = Users.IdInformation
        WHERE NomUtilisateur = ? OR Email = ?
        ''', (user, user))
        users = cursor.fetchone()
        if users:
            user_pswd = users[2]
            if check_password_hash(user_pswd, password):
                session['loggedin'] = True
                session['Id'] = users[0]
                session['username'] = users[1]
                return redirect(url_for('accueil'))
            else:
                flash("Mot de passe incorrect !", 'info')
                return redirect(url_for('connexion'))
        else:
            flash("Identifiant incorrect !", 'info')
            return redirect(url_for('connexion'))
    return render_template("./connexion/connexion.html")


@app.route('/pwdcode')
def pwdcode():
    return render_template("./connexion/pwdcode.html")


@app.route('/pwdreset')
def pwdreset():
    return render_template("./connexion/pwdreset.html")


@app.route('/pwdoublie')
def pwdoublie():
    return render_template("./connexion/pwdoublie.html")


# ................Fin brayane route (Inscription)#


if __name__ == "__main__":
    app.run(debug=True)
