import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.application import MIMEApplication  

def envoicode(code,email):
    
    message = MIMEMultipart()
    message["From"] = 'optimalmedical.sante@gmail.com'
    message["To"] = email
    message["Subject"] = 'Code de vérification'
    
    message.attach(MIMEText(f"Bonjour Monsieur/Madame, \n Votre code de vérification est {code}", "plain")) 
    serveur_smtp = smtplib.SMTP("smtp.gmail.com", 587)
    serveur_smtp.starttls()
    serveur_smtp.login('optimalmedical.sante@gmail.com', 'nhrohjepndcgbrld')
    serveur_smtp.sendmail('optimalmedical.sante@gmail.com', email, message.as_string())
