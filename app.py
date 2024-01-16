from flask import Flask, url_for, render_template, request, flash, redirect, abort, session
from werkzeug.security import generate_password_hash, check_password_hash
from sendcode import envoicode
from datetime import datetime
import os
import requests
import random
import pyodbc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clés_flash'
DSN = 'Driver={SQL Server};Server=DESKTOP-E924B14\\SQLEXPRESS;Database=OptimalMedical;'
app.secret_key = 'OPTIMAL-MEDICAL-KEY'


# Impish_Boy

# Server=DESKTOP-FRGCPSS\\SQLEXPRESS


@app.route('/monhopital')
def monhopital():
    if 'username' in session:
        lien = session.get('lien')
        idinformation = session.get('idinformation')
        conn = pyodbc.connect(DSN)
        cursor = conn.cursor()

        cursor.execute('''
        SELECT * FROM Nomservices 
        ''')
        nomservices = cursor.fetchall()

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

        cursor.execute('''
                SELECT Services.idservice, Services.Nombreplace, NomServices.NomService, Services.placedisponible, Services.attente
                FROM services
                INNER JOIN NomServices ON NomServices.IdNomServices = Services.IdNomService
                where IdInformation = ?
                ''', idinformation)
        services = cursor.fetchall()
        conn.close()

        return render_template("./utilisateur/utilisateurhopital.html", etats=etats, nomservices=nomservices,
                               communes=communes, regions=regions, departements=departements, lien=lien,
                               services=services)
    else:
        return redirect(url_for('accueil'))


@app.route('/plus/<idservice>')
def plus(idservice):
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM services 
        where idService= ?
        ''', idservice)
    services = cursor.fetchone()
    if services[2] > services[3]:
        ch = services[3] + 1
        cursor.execute("UPDATE services SET placedisponible = ? WHERE idservice = ?", (ch, idservice))
        conn.commit()
        return redirect(url_for('monhopital'))
    elif services[2] == services[3]:
        ch = services[4] + 1
        cursor.execute("UPDATE services SET attente = ? WHERE idservice = ?", (ch, idservice))
        conn.commit()
        return redirect(url_for('monhopital'))


@app.route('/moins/<idservice>')
def moins(idservice):
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM services 
        where idService= ?
        ''', idservice)
    services = cursor.fetchone()
    if services[4] > 0:
        ch = services[4] - 1
        cursor.execute("UPDATE services SET attente = ? WHERE idservice = ?", (ch, idservice))
        conn.commit()
        return redirect(url_for('monhopital'))
    elif services[3] > 0:
        ch = services[3] - 1
        cursor.execute("UPDATE services SET placedisponible = ? WHERE idservice = ?", (ch, idservice))
        conn.commit()
        return redirect(url_for('monhopital'))
    else:
        return redirect(url_for('monhopital'))


@app.route('/transfertECR')
def transfertECR():
    lien = session.get('lien')
    iduser = session.get('iduser')
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

    cursor.execute('''
            SELECT transfert.dateheure, InfoDes.Nom, NomServices.NomService , etatpatient.etat, Departement.NomDepartement, Commune.NomCommune
            FROM transfert
            INNER JOIN NomServices ON NomServices.IdNomServices = transfert.IdNomService
            INNER JOIN etatpatient ON etatpatient.Idetatpatient = transfert.Idetatpatient
            INNER JOIN Users AS UsersDes ON Transfert.IdUserDes = UsersDes.IdUser
            INNER JOIN Informations AS InfoDes ON UsersDes.IdInformation = InfoDes.IdInformation
            INNER JOIN Adresses ON Adresses.IdAdresse = InfoDes.IdAdresse
            INNER JOIN Departement ON Departement.IdDepartement = Adresses.IdDepartement
            INNER JOIN Commune ON Adresses.IdCommune = Commune.IdCommune
            where transfert.Iduserdes = ?
                ''', iduser)
    data = cursor.fetchall()

    conn.close()
    return render_template("./utilisateur/transfertECR.html", etats=etats, services=services, communes=communes,
                           regions=regions, departements=departements, lien=lien, data=data)


@app.route('/transferteffectué')
def transferteffectué():
    lien = session.get('lien')
    iduser = session.get('iduser')
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

    cursor.execute('''
               SELECT transfert.dateheure, InfoDes.Nom, NomServices.NomService , etatpatient.etat, Departement.NomDepartement, Commune.NomCommune
               FROM transfert
               INNER JOIN NomServices ON NomServices.IdNomServices = transfert.IdNomService
               INNER JOIN etatpatient ON etatpatient.Idetatpatient = transfert.Idetatpatient
               INNER JOIN Users AS UsersDes ON Transfert.IdUserDes = UsersDes.IdUser
               INNER JOIN Informations AS InfoDes ON UsersDes.IdInformation = InfoDes.IdInformation
               INNER JOIN Adresses ON Adresses.IdAdresse = InfoDes.IdAdresse
               INNER JOIN Departement ON Departement.IdDepartement = Adresses.IdDepartement
               INNER JOIN Commune ON Adresses.IdCommune = Commune.IdCommune
               where transfert.Iduserdes = ?
                   ''', iduser)
    data = cursor.fetchall()
    conn.close()
    return render_template("./utilisateur/transferteffectué.html", etats=etats, services=services, communes=communes,
                           regions=regions, departements=departements, lien=lien, data=data)



@app.route('/transfert', methods=["GET", "POST"])
def transfert():
    lien = session.get('lien')
    idinformation = session.get('idinformation')
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM Nomservices 
    ''')
    nomservices = cursor.fetchall()

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
    SELECT * FROM informations
    where IdInformation != ?
    ''', idinformation)
    departements = cursor.fetchall()
    cursor.execute('''
                SELECT Services.idService, Informations.Nom, Services.Nombreplace, NomServices.NomService, Services.placedisponible, Services.attente
                FROM services
                INNER JOIN NomServices ON NomServices.IdNomServices = Services.IdNomService
                INNER JOIN Informations ON Informations.IdInformation = Services.IdInformation
                where services.IdInformation != ?
                ''', idinformation)
    services = cursor.fetchall()
    conn.close()

    if request.method == "POST":
        index = int(request.form['selectedService'])
        session['index'] = index
        return redirect(url_for('validertransfert'))

    return render_template("./utilisateur/utilisateurtransfert.html", nomservices=nomservices, communes=communes,
                           regions=regions, services=services, departements=departements, lien=lien)


@app.route('/validertransfert', methods=["GET", "POST"])
def validertransfert():
    index = session.get('index')
    lien = session.get('lien')
    idinformation = session.get('idinformation')
    iduser = session.get('iduser')
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM EtatPatient
    ''')
    etatpatient = cursor.fetchall()

    cursor.execute('''
                SELECT Services.idservice, Informations.Nom, NomServices.NomService, Services.IdNomService, users.iduser
                FROM services
                INNER JOIN NomServices ON NomServices.IdNomServices = Services.IdNomService
                INNER JOIN Informations ON Informations.IdInformation = Services.IdInformation
                INNER JOIN users ON users.IdInformation = Services.IdInformation
                where services.Idservice = ?
                ''', index)
    transf = cursor.fetchone()

    cursor.execute('''
                SELECT * from Informations
                where IdInformation = ?
                ''', idinformation)
    Etabdep = cursor.fetchone()

    if request.method == "POST":
        idetat = request.form.get("Etatpat")
        date = datetime.now().strftime("%Y-%m-%d"' '"%H:%M:%S")
        cursor.execute('''insert into transfert (iduserdep, iduserdes, idnomservice, dateheure, idetatpatient) 
                                values(?,?,?,?,?)''', (iduser, transf[4], transf[3], date, idetat))
        conn.commit()
        flash(" transfert en cour!", 'info')
        return redirect(url_for('transfert'))

    return render_template("./utilisateur/confirmetransfert.html", transf=transf, lien=lien, etatpatient=etatpatient,
                           Etabdep=Etabdep)


@app.route('/monprofil')
def monprofil():
    idiformation = session.get('idinformation')
    lien = session.get('lien')
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute("""
                       SELECT * FROM users
                       WHERE IdInformation = ?
                   """, idiformation)
    users = cursor.fetchone()

    cursor.execute("""
                    SELECT informations.Nom, informations.Matricule, Adresses.IdAdresse, Commune.NomCommune, Departement.NomDepartement, Region.NomRegion
                    FROM informations
                    INNER JOIN Adresses ON Adresses.IdAdresse = informations.IdAdresse
                    INNER JOIN Departement ON Departement.IdDepartement = Adresses.IdDepartement
                    INNER JOIN Commune ON Adresses.IdCommune = Commune.IdCommune
                    INNER JOIN Region ON Region.IdRegion = Adresses.IdRegion
                    WHERE IdInformation = ?
                  """, idiformation)
    info = cursor.fetchone()
    cursor.execute("""
                SELECT Services.idservice, Services.Nombreplace, NomServices.NomService
                FROM services
                INNER JOIN NomServices ON NomServices.IdNomServices = Services.IdNomService
                WHERE IdInformation = ?
            """, idiformation)
    services = cursor.fetchall()
    conn.close()
    return render_template("./utilisateur/utilisateurprofil.html", services=services, lien=lien, users=users, info=info)


@app.route('/suppression/<int:id>')
def suppression(id):
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM services WHERE Idservice ={id};")
    conn.commit()
    flash(" Le services a été supprimer avec succès !", 'info')
    return redirect(url_for('monprofil'))


@app.route('/modification/<int:id>', methods=["GET", "POST"])
def modification(id):
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    lien = session.get('lien')
    cursor.execute("""
                SELECT Services.Nombreplace, NomServices.NomService
                FROM services
                INNER JOIN NomServices ON NomServices.IdNomServices = Services.IdNomService
                WHERE Idservice = ?
            """, id)
    service = cursor.fetchone()
    if request.method == "POST":
        capacite = request.form["capacite"]
        cursor.execute("UPDATE services SET nombreplace = ? WHERE idservice = ?", (capacite, id))
        conn.commit()
        conn.close()
        flash(f" La capacite de votre service a été modifieé avec succès !", 'info')
        return redirect(url_for('monprofil'))

    return render_template("./utilisateur/modifservice0.html", service=service, lien=lien)


@app.route('/modificationUsers', methods=["GET", "POST"])
def modificationUsers():
    idiformation = session.get('idinformation')
    lien = session.get('lien')
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute("""
                           SELECT * FROM users
                           WHERE IdInformation = ?
                       """, idiformation)
    users = cursor.fetchone()
    if request.method == "POST":
        Nom = request.form["Nom"]
        cursor.execute("UPDATE users SET NomUtilisateur = ? WHERE IdUser = ?", (Nom))
        conn.commit()
        mot = request.form["mot"]
        cursor.execute("UPDATE users SET Password = ? WHERE IdUser = ?", (mot))
        conn.commit()
        mail = request.form["mail"]
        cursor.execute("UPDATE users SET email = ? WHERE IdUser = ?", (mail))
        conn.commit()
        conn.close()
        flash(f" Vos informations on étè modifier avec succés !", 'info')
        return redirect(url_for('monprofil'))
    return render_template("./utilisateur/modifusers.html", users=users)


@app.route('/modificationLogo', methods=["GET", "POST"])
def modificationLogo():
    idiformation = session.get('idinformation')
    lien = session.get('lien')
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()

    cursor.execute("""
                           SELECT informations.Nom, informations.Matricule
                           FROM informations
                           WHERE IdInformation = ?
                         """, idiformation)
    info = cursor.fetchone()

    return render_template("./utilisateur/modifLogo.html", info=info)


@app.route('/modifinfo', methods=["GET", "POST"])
def modifinfo():
    idiformation = session.get('idinformation')
    lien = session.get('lien')
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()

    cursor.execute("""
                        SELECT informations.Nom, informations.Matricule, Adresses.IdAdresse, Commune.NomCommune, Departement.NomDepartement, Region.NomRegion
                        FROM informations
                        INNER JOIN Adresses ON Adresses.IdAdresse = informations.IdAdresse
                        INNER JOIN Departement ON Departement.IdDepartement = Adresses.IdDepartement
                        INNER JOIN Commune ON Adresses.IdCommune = Commune.IdCommune
                        INNER JOIN Region ON Region.IdRegion = Adresses.IdRegion
                        WHERE IdInformation = ?
                      """, idiformation)
    info = cursor.fetchone()

    if request.method == "POST":
        Nom = request.form["Nom"]
        cursor.execute("UPDATE informations SET Nom = ? WHERE IdInformation = ?", (Nom))
        conn.commit()
        matricule = request.form["matricule"]
        cursor.execute("UPDATE informations SET Matricule = ? WHERE IdInformation = ?", (matricule))
        conn.commit()
        conn.close()
        flash(f" Vos informations on étè modifier avec succés !", 'info')
        return redirect(url_for('monprofil'))
    return render_template("./utilisateur/modifinfo.html", info=info)

@app.route('/inscriptioninfos', methods=["GET", "POST"])
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

        conn = pyodbc.connect(DSN)
        cursor = conn.cursor()

        nom = request.form['Nom']
        num = request.form['Num']
        tel = request.form['Tel']

        cursor.execute(''' SELECT * FROM Informations 
                            WHERE Nom = ?
                            ''', nom)
        a = cursor.fetchone()
        cursor.execute(''' SELECT * FROM Informations 
                            WHERE Matricule = ?
                            ''', num)
        b = cursor.fetchone()
        cursor.execute(''' SELECT * FROM Informations 
                            WHERE Telephone = ?
                            ''', tel)
        c = cursor.fetchone()
        if a:
            flash("Ce nom exist déjà!", 'info')

        elif b:
            flash("Matricule déjà existant!", 'info')

        elif c:
            flash(" déjà existant!", 'info')

        else:
            nCommune = request.form['selected_value3']
            ndepartement = request.form['selected_value2']
            nregion = request.form['selected_value1']
            if nCommune == 'option':
                flash("veillez choisir une commune!", 'info')
            elif ndepartement == 'option':
                flash("veillez choisir un departement!", 'info')
            elif nregion == 'option':
                flash("veillez choisir une region!", 'info')
            else:
                image = request.files['logo']
                if image.filename == '':
                    flash("Aucun fichier sélectionné !", 'info')
                else:
                    url = f'static/img/{nom}/'
                    if not os.path.exists(url):
                        os.makedirs(url)
                    image.save(url + image.filename)

                    try:
                        response = requests.get('https://ipinfo.io/json')
                        data = response.json()
                        coordinates = data['loc'].split(',')
                        latitude = coordinates[0]
                        longitude = coordinates[1]
                    except Exception as e:
                        latitude = None
                        longitude = None

                    localisation = latitude + ' ' + longitude
                    idadresse = tel[-10:]
                    cursor.execute('''insert into Adresses (idadresse,idCommune, idDepartement, idRegion,positiongeo) 
                                values(?,?,?,?,?)''', (idadresse, nCommune, ndepartement, nregion, localisation))
                    conn.commit()

                    cursor.execute('''INSERT INTO Informations (Nom, Matricule, Telephone, idadresse,lienimg)
                                VALUES (?, ?, ?,?,?)''', (nom, num, tel, idadresse, url + image.filename))
                    conn.commit()

                    cursor.execute(''' SELECT * FROM Informations 
                                        WHERE Matricule = ?
                                        ''', num)
                    idinformation = cursor.fetchone()
                    session['idinformation'] = idinformation[0]
                    conn.close()
                    return redirect(url_for('listeservice'))
    return render_template("./inscription/inscriptioninfos.html", Region=Region, Departement=Departement,
                           Commune=Commune)


@app.route('/ListeService', methods=["GET", "POST"])
def listeservice():
    idiformation = session.get('idinformation')
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute("""
                SELECT Services.idservice, Services.Nombreplace, NomServices.NomService
                FROM services
                INNER JOIN NomServices ON NomServices.IdNomServices = Services.IdNomService
                WHERE IdInformation = ?
            """, idiformation)
    services = cursor.fetchall()
    conn.close()
    return render_template("./inscription/inscriptionservice.html ", services=services)


@app.route('/AjoutService', methods=["GET", "POST"])
def ajoutservice():
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM Nomservices 
    ''')
    services = cursor.fetchall()
    if request.method == "POST":
        idinformation = session.get('idinformation')
        service = request.form['selected_value']
        capacite = request.form['capacite']
        disponible = 0
        attente = 0
        cursor.execute('''INSERT INTO services (idnomservice, Nombreplace, placedisponible, attente, idinformation)
                       VALUES (?, ?, ?, ?, ?)''', (service, capacite, disponible, attente, idinformation))
        conn.commit()
        conn.close()
        return redirect(url_for('listeservice'))
    return render_template("./inscription/inscriptionservice0.html ", services=services)


@app.route("/confirmsupservice/<int:item_id>", methods=['GET', 'POST'])
def confirmsupservice(item_id):
    item_id = int(item_id)
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM services WHERE IdService = ?', item_id)
    data = cursor.fetchone()
    conn.commit()
    conn.close()
    return render_template("./inscription/confirm_sup_service.html", data=data)


@app.route('/supprimerservice/<int:item_id>', methods=['GET', 'POST'])
def supprimerservice(item_id):
    item_id = int(item_id)
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM services WHERE IdService = ?', item_id)
    conn.commit()
    conn.close()
    flash(f'Le service numéro {item_id} a été supprimé avec succès !', 'info')
    return redirect(url_for('listeservice'))


@app.route('/modifierservice/<int:item_id>', methods=['GET', 'POST'])
def modifierservice(item_id):
    item_id = int(item_id)
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM services WHERE IdService = ?', item_id)
    data = cursor.fetchone()
    cursor.execute('''
        SELECT * FROM Nomservices 
        ''')
    services = cursor.fetchall()
    if request.method == 'POST':
        nom = request.form['nom']
        categorie = request.form['categorie']
        prixunitaire = request.form['prixunitaire']
        cursor.execute('''
            UPDATE produit
            SET NomProduit = ?, CatProduit = ?, PrixUnitaire = ?
            WHERE IdProduit = ?
        ''', (nom, categorie, prixunitaire, item_id))
        conn.commit()
        conn.close()
        flash(f'Le produit numéro {item_id} a été modifié avec succès !', 'info')
        return redirect(url_for('afficherproduit'))
    return render_template('./inscription/modifierservice.html', data=data, services=services)


@app.route('/inscriptionacces', methods=["GET", "POST"])
def inscriptionacces():
    if request.method == 'POST':
        idinformation = session.get('idinformation')
        user = request.form["username"]
        mail = request.form["email"]
        password = request.form["password"]
        password1 = request.form["password1"]
        conn = pyodbc.connect(DSN)
        cursor = conn.cursor()

        cursor.execute(''' SELECT * FROM users 
                            WHERE NomUtilisateur = ?
                            ''', user)
        b = cursor.fetchone()

        cursor.execute(''' SELECT * FROM users 
                            WHERE email = ?
                            ''', mail)
        c = cursor.fetchone()

        if b:
            flash("NomUtilisateur déjà existant!", 'alert')

        elif c:
            flash("Email déjà existant!", 'alert')

        else:
            if len(password) < 8:
                flash("le mot de passe doit être superieur ou égal à 8 caractère!", 'alert')
            elif password != password1:
                flash("Repétez le même mot de passe!", 'alert')
            else:
                categorie = 'Attente'
                cursor.execute('''INSERT INTO users (nomutilisateur, email, password,idinformation,categorie)
                            VALUES (?, ?, ?,?,?)''', (user, mail, generate_password_hash(password),
                                                      idinformation, categorie))
                conn.commit()
                conn.close()
                return redirect(url_for('connexion'))
    return render_template("./inscription/inscriptionacces.html")


#     connexion


@app.route("/", methods=["GET", "POST"])
def accueil():
    if 'username' in session:
        if session['username'] == 'admin':
            return redirect(url_for('admin'))
        else:
            return redirect(url_for("monhopital"))
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
        WHERE NomUtilisateur = ? OR email = ?
        ''', (user, user))
        user = cursor.fetchone()
        if user:
            pswd = user[3]
            if check_password_hash(pswd, password):
                if user[-1] == 'OK':
                    cursor.execute('''
                                SELECT * FROM informations 
                                WHERE idinformation = ? 
                                ''', (user[4]))
                    lien = cursor.fetchone()
                    lien = lien[5][6:]
                    session['loggedin'] = True
                    session['username'] = user[1]
                    session['iduser'] = user[0]
                    session['lien'] = lien
                    session['idinformation'] = user[4]
                    return redirect(url_for('accueil'))
                else:
                    return redirect(url_for('reclamation'))
            else:
                flash("Mot de passe incorrect !", 'error')
        else:
            flash("Identifiant incorrect !", 'error')
    return render_template("./connexion/connexion.html")


@app.route('/reclamation', methods=["GET", "POST"])
def reclamation():
    #    if 'loggedin' in session:
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()

    return render_template("./connexion/reclamation.html", )


#    return redirect(url_for('connexion'))


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
                        ''', (password, email))
            conn.commit()
            conn.close()
            flash('votre mot de passe à bien été modifié, connectez vous')
            return redirect(url_for('connexion'))
        else:
            flash('veillez saisir le même mot de passe dans les deux champs')
    return render_template("./connexion/pwdreset.html")


# ................yesufu route (Admin)#


@app.route('/admin')
def admin():
    if 'loggedin' in session:
        conn = pyodbc.connect(DSN)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM Informations """)
        inscrit = cursor.fetchall()
        nbrinscrit = len(inscrit)
        cursor.execute(""" SELECT * FROM Transfert """)
        transfert = cursor.fetchall()
        nbrtransfert = len(transfert)
        cursor.execute(""" SELECT * FROM Reclamation """)
        reclamation = cursor.fetchall()
        nbrreclamation = len(reclamation)
        cursor.execute(""" SELECT TOP 5 Nom, Matricule, Telephone
                            FROM Informations
                            ORDER BY IdInformation DESC """)
        inscritrec = cursor.fetchall()
        cursor.execute("""
                        SELECT InfoDep.Nom, InfoDes.Nom, NomServices.NomService, EtatPatient.Etat, Transfert.Dateheure
                        FROM Transfert 
                        INNER JOIN Users AS UsersDep ON Transfert.IdUserDep = UsersDep.IdUser
                        INNER JOIN Users AS UsersDes ON Transfert.IdUserDes = UsersDes.IdUser
                        INNER JOIN Informations AS InfoDep ON UsersDep.IdInformation = InfoDep.IdInformation
                        INNER JOIN Informations AS InfoDes ON UsersDes.IdInformation = InfoDes.IdInformation
                        INNER JOIN NomServices ON NomServices.IdNomServices = Transfert.IdNomService
                        INNER JOIN EtatPatient ON Transfert.IdEtatPatient = EtatPatient.IdEtatPatient
                        """)
        historique = cursor.fetchall()
        conn.close()
        return render_template("./admin/admin.html", nbrinscrit=nbrinscrit, nbrtransfert=nbrtransfert,
                               nbrreclamation=nbrreclamation, inscritrec=inscritrec, historique=historique)
    return redirect(url_for('connexion'))


@app.route('/historique')
def historique():
    if 'loggedin' in session:
        conn = pyodbc.connect(DSN)
        cursor = conn.cursor()
        cursor.execute("""
                    SELECT InfoDep.Nom, InfoDes.Nom, NomServices.NomService, EtatPatient.Etat, Transfert.Dateheure
                    FROM Transfert 
                    INNER JOIN Users AS UsersDep ON Transfert.IdUserDep = UsersDep.IdUser
                    INNER JOIN Users AS UsersDes ON Transfert.IdUserDes = UsersDes.IdUser
                    INNER JOIN Informations AS InfoDep ON UsersDep.IdInformation = InfoDep.IdInformation
                    INNER JOIN Informations AS InfoDes ON UsersDes.IdInformation = InfoDes.IdInformation
                    INNER JOIN NomServices ON NomServices.IdNomServices = Transfert.IdNomService
                    INNER JOIN EtatPatient ON Transfert.IdEtatPatient = EtatPatient.IdEtatPatient
                """)
        data = cursor.fetchall()
        conn.close()
        return render_template("./admin/historiqueadmin.html", data=data)
    return redirect(url_for('connexion'))


@app.route('/demande')
def demande():
    if 'loggedin' in session:
        conn = pyodbc.connect(DSN)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT Informations.IdInformation, Informations.Matricule, Informations.Nom, Users.email, Commune.NomCommune, Departement.NomDepartement
            , Region.NomRegion, Informations.Telephone, Users.categorie
            FROM Informations, Users, Adresses, Commune, Departement, Region
            WHERE Informations.IdInformation = Users.IdInformation AND Informations.IdAdresse = Adresses.IdAdresse
            AND Adresses.IdCommune = Commune.IdCommune
            AND Adresses.IdDepartement = Departement.IdDepartement
            AND Adresses.IdRegion = Region.IdRegion
            AND Users.categorie = 'Attente'
            AND Users.NomUtilisateur <> 'admin'
        """)
        data = cursor.fetchall()
        conn.close()
        return render_template("./admin/demandeadmin.html", data=data)
    return redirect(url_for('connexion'))


@app.route('/monprofiladmin/<int:item_id>', methods=['GET', 'POST'])
def monprofiladmin(item_id):
    if 'loggedin' in session:
        item_id = int(item_id)
        lien = session.get('lien')
        conn = pyodbc.connect(DSN)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Region")
        Region = cursor.fetchall()
        cursor.execute("SELECT * FROM Departement")
        Departement = cursor.fetchall()
        cursor.execute("""
                        SELECT NomServices.NomService, Services.Nombreplace 
                        FROM services
                        INNER JOIN NomServices ON NomServices.IdNomServices = Services.IdNomService
                        WHERE IdInformation = ?
                    """, item_id)
        services = cursor.fetchall()
        cursor.execute("SELECT * FROM Commune")
        Commune = cursor.fetchall()
        cursor.execute('''
        SELECT Informations.IdInformation, Users.NomUtilisateur, Informations.Telephone, Informations.Nom, 
        Informations.Matricule, Commune.IdCommune, Commune.NomCommune, Adresses.IdDepartement, 
        Departement.NomDepartement, Region.IdRegion, Region.NomRegion, Informations.IdAdresse, Users.email, 
        Informations.lienimg
        FROM Informations
        INNER JOIN Users ON Users.IdInformation = Informations.IdInformation
        INNER JOIN Adresses ON Adresses.IdAdresse = Informations.IdAdresse
        INNER JOIN Commune ON Adresses.IdCommune = Commune.IdCommune
        INNER JOIN Departement ON Departement.IdDepartement = Adresses.IdDepartement
        INNER JOIN Region ON Adresses.IdRegion = Region.IdRegion
        WHERE Informations.IdInformation = ?
        ''', item_id)
        data = cursor.fetchone()
        if request.method == 'POST':
            validation = 'OK'
            cursor.execute('''
                UPDATE Users
                SET Users.categorie = ?
                FROM Users
                INNER JOIN Informations ON Users.IdInformation = Informations.IdInformation
                WHERE Informations.IdInformation = ?
            ''', (validation, item_id))
            conn.commit()
            conn.close()
            flash(f"L'établissement numéro {item_id} est désormais inscrit !", 'info')
            return redirect(url_for('demande'))

        return render_template('./admin/utilisateurprofiladmin.html', data=data, ListeRegion=Region,
                               ListeDepartement=Departement, ListeCommune=Commune, lien=lien, services=services)
    return redirect(url_for('connexion'))


@app.route('/listeinscrit')
def listeinscrit():
    if 'loggedin' in session:
        conn = pyodbc.connect(DSN)
        cursor = conn.cursor()
        cursor.execute("""
                    SELECT Informations.IdInformation, Informations.Matricule, Informations.Nom, Users.email, Commune.NomCommune, Departement.NomDepartement
                    , Region.NomRegion, Informations.Telephone, Users.categorie
                    FROM Informations, Users, Adresses, Commune, Departement, Region
                    WHERE Informations.IdInformation = Users.IdInformation AND Informations.IdAdresse = Adresses.IdAdresse
                    AND Adresses.IdCommune = Commune.IdCommune
                    AND Adresses.IdDepartement = Departement.IdDepartement
                    AND Adresses.IdRegion = Region.IdRegion
                    AND Users.NomUtilisateur <> 'admin'
                    AND Users.categorie = 'OK'
                """)
        data = cursor.fetchall()
        conn.close()
        return render_template("./admin/listeinscrit.html", data=data)
    return redirect(url_for('connexion'))


@app.route('/viewprofiladmin/<int:item_id>', methods=['GET', 'POST'])
def viewprofiladmin(item_id):
    if 'loggedin' in session:
        item_id = int(item_id)
        lien = session.get('lien')
        conn = pyodbc.connect(DSN)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Region")
        Region = cursor.fetchall()
        cursor.execute("SELECT * FROM Departement")
        Departement = cursor.fetchall()
        cursor.execute("""
                        SELECT NomServices.NomService, Services.Nombreplace 
                        FROM services
                        INNER JOIN NomServices ON NomServices.IdNomServices = Services.IdNomService
                        WHERE IdInformation = ?
                    """, item_id)
        services = cursor.fetchall()
        cursor.execute("SELECT * FROM Commune")
        Commune = cursor.fetchall()
        cursor.execute('''
        SELECT Informations.IdInformation, Users.NomUtilisateur, Informations.Telephone, Informations.Nom, 
        Informations.Matricule, Commune.IdCommune, Commune.NomCommune, Adresses.IdDepartement, 
        Departement.NomDepartement, Region.IdRegion, Region.NomRegion, Informations.IdAdresse, Users.email, 
        Informations.lienimg
        FROM Informations
        INNER JOIN Users ON Users.IdInformation = Informations.IdInformation
        INNER JOIN Adresses ON Adresses.IdAdresse = Informations.IdAdresse
        INNER JOIN Commune ON Adresses.IdCommune = Commune.IdCommune
        INNER JOIN Departement ON Departement.IdDepartement = Adresses.IdDepartement
        INNER JOIN Region ON Adresses.IdRegion = Region.IdRegion
        WHERE Informations.IdInformation = ?
        ''', item_id)
        data = cursor.fetchone()
        return render_template('./admin/utilisateurprofiladmin0.html', data=data, ListeRegion=Region,
                               ListeDepartement=Departement, ListeCommune=Commune, lien=lien, services=services)
    return redirect(url_for('connexion'))


@app.route("/deconnexion")
def deconnexion():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('connexion'))


# ................Fin yesufu route (Admin)#


if __name__ == "__main__":
    app.run(debug=True)
