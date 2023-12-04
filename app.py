from flask import Flask, url_for, render_template, request, flash, redirect, abort, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)




#  utilisateurs 


@app.route('/monhopital')
def monhopital():
    return render_template("./utilisateur/utilisateurhôpital.html")


@app.route('/monprofil')
def monprofil():
    return render_template("./utilisateur/utilisateurprofil.html")


@app.route('/transfert')
def transfert():
    return render_template("./utilisateur/utilisateurtransfert.html")


# ................brayane route (Inscription)#

@app.route('/inscriptioninfos')
def inscriptioninfos():
    return render_template("./inscription/inscriptioninfos.html")


@app.route('/inscriptionacces')
def inscriptionacces():
    data = ''
    return render_template("./inscription/inscriptionacces.html", data=data)


@app.route('/ListeService')
def ListeService():
    return render_template("./inscription/inscriptionservice.html ")


@app.route('/AjoutService')
def AjoutService():
    return render_template("./inscription/inscriptionservice0.html ")


<<<<<<< HEAD
# ................Fin brayane route (Inscription)#
=======
#     connexion 

@app.route('/')
def Connexion():
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

#................Fin brayane route (Inscription)#
>>>>>>> 6ffb3c69d4e9d0da3abb3d9800ab5675e0982269


if __name__ == "__main__":
    app.run(debug=True)
