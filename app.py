from flask import Flask, url_for, render_template, request, flash, redirect, abort, session
from werkzeug.security import generate_password_hash, check_password_hash
from sendcode import envoicode
import random
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
        WHERE Users.NomUtilisateur = ? OR Users.Email = ?
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

href="{{ url_for('ajout', type=cat) }}"

@app.route('/pwdoublie',methods=["GET", "POST"])
def pwdoublie():
    if request.method == 'POST':
        user = request.form["text"]
        conn = pyodbc.connect(DSN)
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM Users 
        WHERE NomUtilisateur = ? OR Email = ?
        ''', (user, user))
        users = cursor.fetchone()
        conn.close()
        if users:
            code =''.join([str(random.randint(0, 9)) for _ in range(4)])
            session['code'] = code
            session['email']=users[4]
            envoicode(code,users[4])
            return redirect(url_for('pwdcode'))
        else:
            flash('le mail ou le nom d\'utilisateur n\'existe pas')
    return render_template("./connexion/pwdoublie.html")


@app.route('/pwdcode',methods=["GET", "POST"])
def pwdcode():
    code = session.get('code')
    if not code:
        flash('Code introuvable, veuillez demander un nouveau code')
        return redirect(url_for('pwdoublie'))
    if request.method == 'POST':
        codesaisir = request.form["code"]
        if  codesaisir==code:
            return redirect(url_for('pwdreset'))
        else:
            flash('veillez saisir le bon code de validation')
    return render_template("./connexion/pwdcode.html")


@app.route('/pwdreset',methods=["GET", "POST"])
def pwdreset():
    email = session.get('email')
    if request.method == 'POST':
        password = request.form["password"]
        password1 = request.form["password"]
        if password1==password:
            password=generate_password_hash(password)
            conn = pyodbc.connect(DSN)
            cursor = conn.cursor()
            cursor.execute(f'''
                        UPDATE users
                        SET Password = ?
                        WHERE  Email = ?
                        ''', (email, password))
            conn.commit()
            conn.close()
            flash('votre mot de passe à bien été modifié, connectez vous')
            return redirect(url_for('connexion'))
        else:
            flash('veillez saisir le même mot de passe dans les deux champs')
    return render_template("./connexion/pwdreset.html")

# ................Fin brayane route (Inscription)#


if __name__ == "__main__":
    app.run(debug=True)
