import os, re, smtplib, platform                          
from email.mime.text import MIMEText    
import services_utilitaires as util

"""
Cette classe permet au serveur de rendre des services.
"""
class Services:
    def __init__(self, server_socket):
        self.server_socket = server_socket

    """
    Cette fonction permet de recevoir une requete d'un client, de l'identifier et
    de fournir le service associé à la requete.
    """
    def fournir(self):
        self.server_socket.accept_client()
        requete = self.server_socket.receive()
        if requete == "UTILISATEUR_EXISTE":
            msg = self.server_socket.receive()
            self.server_socket.send(Services.utilisateur_existe(msg))
        elif requete == "PASSWORD_MATCHES":
            username, password = self.server_socket.receive()
            self.server_socket.send(Services.password_matches(username, password))
        elif requete == "PASSWORD_VALIDITY":
            password = self.server_socket.receive()
            self.server_socket.send(Services.password_validity(password))
        elif requete == "INSCRIRE_UTILISATEUR":
            username, password = self.server_socket.receive()
            self.server_socket.send(Services.inscrire_utilisateur(username, password))
        elif requete == "ENVOYER_COURRIEL":
            mailfrom, rcptto, subjet, text = self.server_socket.receive()
            self.server_socket.send(Services.envoyer_courriel(mailfrom, rcptto, subjet, text))
        elif requete == "CONSULTER_LISTE_COURRIELS":
            utilisateur = self.server_socket.receive()
            self.server_socket.send(Services.consulter_liste_courriels(utilisateur))
        elif requete == "CONSULTER_COURRIEL":
            utilisateur = self.server_socket.receive()
            numero_courriel = self.server_socket.receive()
            self.server_socket.send(Services.consulter_courriel(utilisateur, numero_courriel))
        elif requete == "OBTENIR_NOMBRE_MESSAGES":
            utilisateur = self.server_socket.receive()
            self.server_socket.send(Services.obtenir_nombre_messages(utilisateur))
        elif requete == "OBTENIR_TAILLE_DOSSIER":
            utilisateur = self.server_socket.receive()
            self.server_socket.send(Services.obtenir_taille_dossier(utilisateur))
        else:
            print("\t!!   SERVICE_INVALIDE")
        self.server_socket.leave_client()
    
    
    #--SERVICES-----------------------------------------------------------------------    
    """
    Cette fonction indique si un nom d'utilisateur donné correspond à un utilisateur existant.
    Elle retourne un bool signifiant si l'utilisateur existe.
    """
    @staticmethod
    def utilisateur_existe(username):
        return os.path.isdir(util.get_server_path() + username)
    

    """
    Cette fonction indique si un nom d'utilisateur donné correspond à un mot de passe donné.
    Elle retourne un bool signifiant si c'est le cas.
    """
    @staticmethod
    def password_matches(username, given_password):
        password_matches = False
        if Services.utilisateur_existe(username):
            f = open(util.get_server_path() + username + "/config.txt", 'r')
            password = f.readline().splitlines()[0]
            password_matches = password == util.hash(given_password)
        return password_matches

    """
    Cette fonction indique si un mot de passe donné correspond aux critères de validité d'un mot de passe.
    Elle retourne un bool signifiant si le mot de passe est valide.
    """
    @staticmethod
    def password_validity(password):
        return bool(re.search(r"(?=.*\d)(?=.*[a-zA-Z])(?=^.{6,12}$)", password))

    """
    Cette fonction permet d'inscrire un utilisateur sur le serveur.
    Elle retourne un booléen signifiant si l'inscription a réussi.
    """
    @staticmethod
    def inscrire_utilisateur(username, password):
        dossier = util.get_server_path() + username
        os.mkdir(dossier)
        success = True
        try:
            filename = dossier + "/config.txt"
            f = open(filename, 'w')
            f.write(util.hash(password))
            f.close()
        except Exception as e:
            print("Exception: " + str(e))
            print("L'inscription de " + username + " a échoué car son fichier de configuration n'a pas pu être créé.")
            os.rmdir(dossier)
            success = False
        return success
    
    """
    Cette fonction permet d'envoyer un courriel.
    Elle retourne un booléen signifiant si le message a bien été envoyé.
    """
    @staticmethod
    def envoyer_courriel(mailfrom, mailto, subject, text):
        msg = MIMEText(text)
        msg["From"] = mailfrom
        msg["To"] = mailto
        msg["Subject"] = subject
        succes = True
        if util.is_internal_address(mailto):
            succes = Services.envoyer_courriel_interne(mailfrom, mailto, subject, msg)
        else:
            succes = Services.envoyer_courriel_externe(mailfrom, mailto, msg)
        return succes

    """
    Cette fonction est une extrapolation de envoyer_courriel et permet d'envoyer un courriel
    à un utilisateur inscrit sur le serveur.
    """
    @staticmethod
    def envoyer_courriel_interne(mailfrom, mailto, subject, msg):
        message = msg.as_string().split('\n', 3)[3]
        nom_fichier = '/1_' + mailfrom + '_' + subject + ".txt"
        if os.path.isdir(util.get_server_path() + mailto):
            dir_name = util.get_server_path() + mailto
        else:
            dir_name = util.get_server_path() + "DESTERREUR"
            if not os.path.isdir(dir_name):
                os.mkdir(dir_name)
        if util.fichier_numero_un_existe(util.list_files(dir_name)):
            util.incrementer_numero_fichiers(dir_name)
        nom_fichier = dir_name + nom_fichier
        f = open(nom_fichier, 'w')
        f.write(message)
        f.close()
        return True


    """
    Cette fonction est une extrapolation de envoyer_courriel et permet d'envoyer un courriel
    à une adresse ne se terminant pas par @reseauglo.ca
    """
    @staticmethod
    def envoyer_courriel_externe(mailfrom, mailto, msg):
        succes = True
        try:
            smtpConnection = smtplib.SMTP(host="smtp.ulaval.ca", timeout=10)
            smtpConnection.sendmail(mailfrom, mailto, msg.as_string())
            smtpConnection.quit()
            print("Message envoyé.")
        except:
            print("L’envoi n’a pas pu être effectué.")
            succes = False
        return succes

    """
    Cette fonction retourne une liste de courriels d'un utilisateur donné sous forme de string.
    """
    @staticmethod
    def consulter_liste_courriels(utilisateur):
        files = util.list_files(util.get_server_path() + utilisateur)
        print(files)
        courriels = ""
        for f in files:
            if f.split('_')[0].isdigit():
                numero = '[{:1}]'.format(f.split('_')[0])
                mailfrom = f.split('_')[1]
                subject = f.split('_')[2][:-4]
                courriel = '{:7} {:30} {:1}'.format(numero, mailfrom, subject)
                courriels = courriels + '\n' + courriel
        return courriels

    """
    Cette fonction retourne un courriel sous forme de string selon un utilisateur et un numéro de courriel donné.
    """
    @staticmethod
    def consulter_courriel(utilisateur, numero_courriel):
        files = util.list_files(util.get_server_path() + utilisateur)
        for f in files:
            if f.startswith(numero_courriel + '_'):
                f = open(util.get_server_path() + utilisateur + '/' + f, 'r')
                courriel = f.read()
                f.close()
                return courriel

    """
    Cette fonction retourne le nombre de messages qu'un utilisateur donné en argument a dans son répertoire.
    """
    @staticmethod
    def obtenir_nombre_messages(utilisateur):
        files = util.list_files(util.get_server_path() + utilisateur)
        return len(files) - 1

    """
    Cette fonction retourne le nombre d'octets utilisés par le répertoire d'un utilisateur donné en argument.
    """
    @staticmethod
    def obtenir_taille_dossier(utilisateur):
        files = util.list_files(util.get_server_path() + utilisateur)
        dir_size = 0
        for f in files:
            dir_size += os.path.getsize(util.get_server_path() + utilisateur + '/' + f)
        return dir_size

