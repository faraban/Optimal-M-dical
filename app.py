from flask import Flask, url_for, render_template, request, flash, redirect, abort, session
from werkzeug.security import generate_password_hash, check_password_hash
from sendcode import envoicode
import random
import pyodbc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clés_flash'
DSN = 'Driver={SQL Server};Server=y_muhamad\\SQLEXPRESS;Database=OptimalMedical;'


#  utilisateurs

@app.route('/monhopital')
def monhopital():
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM Nomservices 
    ''')
    services = cursor.fetchall()

    cursor.execute('''
    SELECT * FROM commune 
    ''')
    communes = cursor.fetchall()

    cursor.execute('''
    SELECT * FROM region 
    ''')
    regions = cursor.fetchall()

    cursor.execute('''
    SELECT * FROM departement 
    ''')
    departements = cursor.fetchall()

    cursor.execute('''
    SELECT * FROM EtatPatient 
    ''')
    etats = cursor.fetchall()
    conn.close()
    return render_template("./utilisateur/utilisateurhôpital.html", etats=etats, services=services,
                           communes=communes, regions=regions, departements=departements)


@app.route('/monprofil')
def monprofil():

    return render_template("./utilisateur/utilisateurprofil.html")


@app.route('/transfert', methods=["GET", "POST"])
def transfert():
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT * FROM Nomservices 
    ''')
    service = cursor.fetchall()
    services = service[1]

    cursor.execute('''
    SELECT * FROM commune 
    ''')
    commune = cursor.fetchall()
    communes = commune[1]

    cursor.execute('''
    SELECT * FROM region 
    ''')
    region = cursor.fetchall()
    regions = region[1]

    cursor.execute('''
    SELECT * FROM departement 
    ''')
    departements = cursor.fetchall()
    conn.close()

    return render_template("./utilisateur/utilisateurtransfert.html", services=services,
                           communes=communes, regions=regions, departements=departements)


@app.route('/confirmetransfert')
def confirmetransfert():

    return render_template("./utilisateur/confirmetransfert.html")



@app.route('/inscriptioninfos',methods=["GET", "POST"])
def inscriptioninfos():
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Region")
    Region = cursor.fetchall()
    cursor.execute("SELECT * FROM Departement")
    Departement = cursor.fetchall()
    cursor.execute("SELECT * FROM Commune")
    Commune = cursor.fetchall()
    conn.close()
    if request.method == "POST":
        nom = request.form['Nom'] 
        num = request.form['Num'] 
        tel = request.form['Tel']
        Commune = request.form['selected_value3']
        departement = request.form['selected_value2']
        region = request.form['selected_value1'] 
        idadresse=Commune+departement+region
        conn = pyodbc.connect(DSN) 
        cursor = conn.cursor() 
        
        cursor.execute('''insert into Adresses (idadresse,idCommune, idDepartement, idRegion) 
                       values(?,?,?,?)''',(idadresse,Commune,departement,region))
        conn.commit()
        cursor.execute('''INSERT INTO Informations (Nom, Matricule, Telephone, idadresse)
                       VALUES (?, ?, ?,?)''', (nom, num, tel,idadresse))
        conn.commit()
        cursor.execute(''' SELECT * FROM Informations 
                            WHERE Matricule = ?
                            ''', (num)) 
        idinformation = cursor.fetchone()
        session['idinformation']=idinformation[0]
        conn.close()
        return redirect(url_for('connexion'))

@app.route('/ListeService',methods=["GET", "POST"])
def listeservice():
    idiformation=session.get('idinformation')
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()  
    cursor.execute('''
        SELECT * FROM Informations 
        WHERE idinformation = ?
        ''', (idiformation)) 
    services = cursor.fetchall()
    conn.close()
    return render_template("./inscription/inscriptionservice.html ", services=services)

@app.route('/AjoutService',methods=["GET", "POST"])
def ajoutservice():
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor() 
    cursor.execute('''
    SELECT * FROM Nomservices 
    ''')
    services= cursor.fetchall()
    if request.method == "POST":
        idinformation=session.get('idinformation')
        service = request.form['selected_value']
        capacite = request.form['capacite'] 
        cursor.execute('''INSERT INTO services (Nombreplace, idnomservice, idinformation)
                       VALUES (?, ?, ?)''', (capacite, service,idinformation))
        conn.commit() 
        conn.close()
        return redirect(url_for('listeservice'))
    return render_template("./inscription/inscriptionservice0.html ", services=services)


@app.route('/inscriptionacces',methods=["GET", "POST"])
def inscriptionacces():
    if request.method == 'POST':
        idinformation=session.get('idinformation')
        user = request.form["username"]
        mail = request.form["email"]
        password = request.form["password"]
        conn = pyodbc.connect(DSN)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO users (nomutilisateur, email, password,idinformation)
                       VALUES (?, ?, ?,?)''', (user, mail,generate_password_hash(password),idinformation))
        conn.commit() 
        conn.close()
        return redirect(url_for('connexion'))
    return render_template("./inscription/inscriptionacces.html")

#     connexion 

@app.route("/", methods=["GET", "POST"])
def accueil():
    if 'loggedin' in session:
        if session['username'] == 'admin':
            redirect(url_for('admin'))
        else:
            redirect(url_for('monhopital'))
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
        WHERE NomUtilisateur = ? OR Email = ?
        ''', (user, user))
        user = cursor.fetchone()
        if user:
            user_pswd = user[3]
            if check_password_hash(user_pswd,password):
                session['loggedin'] = True
                session['Id'] = user[0]
                session['username'] = user[1]
                return redirect(url_for('accueil'))
            else:
                flash("Mot de passe incorrect !", 'info')
                return redirect(url_for('connexion'))
        else:
            flash("Identifiant incorrect !", 'info')
    return render_template("./connexion/connexion.html")


@app.route("/deconnexion", methods=["GET", "POST"])
def deconnexion():
    session.clear()
    return redirect(url_for('connexion'))

@app.route('/pwdoublie', methods=["GET", "POST"])
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
            code = ''.join([str(random.randint(0, 9)) for _ in range(4)])
            session['code'] = code
            session['email'] = users[2]
            envoicode(code, users[2])
            return redirect(url_for('pwdcode'))
        else:
            flash('le mail ou le nom d\'utilisateur n\'existe pas')
    return render_template("./connexion/pwdoublie.html")


@app.route('/pwdcode', methods=["GET", "POST"])
def pwdcode():
    code = session.get('code')
    if not code:
        flash('Code introuvable, veuillez demander un nouveau code')
        return redirect(url_for('pwdoublie'))
    if request.method == 'POST':
        codesaisir = request.form["code"]
        if codesaisir == code:
            return redirect(url_for('pwdreset'))
        else:
            flash('veillez saisir le bon code de validation')
    return render_template("./connexion/pwdcode.html")


@app.route('/pwdreset', methods=["GET", "POST"])
def pwdreset():
    email = session.get('email')
    if request.method == 'POST':
        password = request.form["password"]
        password1 = request.form["password"]
        if password1 == password:
            password = generate_password_hash(password)
            conn = pyodbc.connect(DSN)
            cursor = conn.cursor()
            cursor.execute(f'''
                        UPDATE users
                        SET Password = ?
                        WHERE  Email = ?
                        ''', (password,email))
            conn.commit()
            conn.close()
            flash('votre mot de passe à bien été modifié, connectez vous')
            return redirect(url_for('connexion'))
        else:
            flash('veillez saisir le même mot de passe dans les deux champs')
    return render_template("./connexion/pwdreset.html")


# ................Fin brayane route (Inscription)#


# ................yesufu route (Admin)#


@app.route('/admin')
def admin():
    return render_template("./admin/admin.html")


@app.route('/historique')
def historique():
    return render_template("./admin/historiqueadmin.html")


@app.route('/demande')
def demande():
#    if 'loggedin' in session:
        conn = pyodbc.connect(DSN)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT Informations.Matricule, Informations.Nom, Users.email, Commune.NomCommune, Departement.NomDepartement
            , Region.NomRegion, Informations.Telephone
            FROM Informations, Users, Adresses, Commune, Departement, Region
            WHERE Informations.IdInformation = Users.IdInformation AND Informations.IdAdresse = Adresses.IdAdresse
            AND Adresses.IdCommune = Commune.IdCommune
            AND Adresses.IdDepartement = Departement.IdDepartement
            AND Adresses.IdRegion = Region.IdRegion
        """)
        data = cursor.fetchall()
        conn.close()
        return render_template("./admin/demandeadmin.html", data=data)
#    return redirect(url_for('connexion'))


@app.route('/listeinscrit')
def listeinscrit():
    return render_template("./admin/listeinscrit.html")


# ................Fin yesufu route (Admin)#


if __name__ == "__main__":
    app.run(debug=True)
