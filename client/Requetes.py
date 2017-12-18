"""
Cette classe permet au client d'identifier et de faire des demandes au serveur.
Pour ce faire, elle utilise un socket contenu par la classe Socket.
"""

class Requetes:
    def __init__(self, socket):
        self.socket = socket

    """
    Cette méthode ne communique exceptionnellement pas avec le serveur.
    Elle permet d'identifier l'utilisateur courant, information nécessaire pour certaines requêtes.
    """
    def set_current_user(self, username):
        self.current_user = username

    """
    Cette méthode ne communique exceptionnellement pas avec le serveur.
    Elle permet de connaître l'utilisateur courant.
    """
    def get_current_user(self):
        return self.current_user
    
    """
    Cette méthode demande au serveur si un nom d'utilisateur donné existe déjà.
    Elle retourne un bool ou None si le serveur est inaccessible.
    """
    def utilisateur_existe(self, username):
        if self.socket.connect():
            self.socket.send("UTILISATEUR_EXISTE")
            self.socket.send(username)
            reponse = self.socket.receive()
            self.socket.disconnect()
            return reponse

    """
    Cette méthode demande au serveur si un nom d'utilisateur et un mot de passe données concordent.
    Elle retourne un bool ou None si le serveur est inaccessible.
    """
    def password_matches(self, username, given_password):
        if self.socket.connect():
            self.socket.send("PASSWORD_MATCHES")
            self.socket.send([username, given_password])
            reponse = self.socket.receive()
            self.socket.disconnect()
            return reponse
    
    """
    Cette méthode demande au serveur d'inscrire un utilisateur en fournissant un nom d'utilisateur et un mot de passe.
    Elle retourne un bool signifiant le succès de l'inscription ou None si le serveur est inaccessible.
    """
    def inscrire_utilisateur(self, username, password):
        if self.socket.connect():
            self.socket.send("INSCRIRE_UTILISATEUR")
            self.socket.send([username, password])
            reponse = self.socket.receive()
            self.socket.disconnect()
            return reponse

    """
    Cette méthode demande au serveur d'envoyer un courriel en fournissant l'utilisateur courant, l'adresse cible, le sujet et le corps du message.
    Elle retourne un bool signifiant le succès de l'envoi ou None si le serveur est inaccessible.
    """
    def envoyer_courriel(self, rcptto, subject, text):
        if self.socket.connect():
            self.socket.send("ENVOYER_COURRIEL")
            self.socket.send([self.current_user, rcptto, subject, text])
            reponse = self.socket.receive()
            self.socket.disconnect()
            return reponse

    """
    Cette méthode permet de consulter la liste de courriel de l'utilisateur courant en fournissant l'utilisateur courant.
    Elle retourne la liste de courriels sous forme de string ou None si le serveur est inaccessible.
    """
    def consulter_liste_courriels(self):
        if self.socket.connect():
            self.socket.send("CONSULTER_LISTE_COURRIELS")
            self.socket.send(self.current_user)
            reponse = self.socket.receive()
            self.socket.disconnect()
            return reponse

    """
    Cette méthode permet de consulter un courriel en particulier en fournissant l'utilisateur et le numéro de courriel à consulter.
    Elle retourne le courriel sous forme de string ou None si le serveur est inaccessible.
    """
    def consulter_courriel(self, choix):
        if self.socket.connect():
            self.socket.send("CONSULTER_COURRIEL")
            self.socket.send(self.current_user)
            self.socket.send(choix)
            reponse = self.socket.receive()
            self.socket.disconnect()
            return reponse

    """
    Cette méthode permet de valider le choix d'un mot de passe selon des critères préalablement affichés à la console.
    Elle retourne un bool signifiant la validité du mot de passe ou Non si le serveur est inaccessible.
    """
    def password_validity(self, password):
        if self.socket.connect():
            self.socket.send("PASSWORD_VALIDITY")
            self.socket.send(password)
            reponse = self.socket.receive()
            self.socket.disconnect()
            return reponse


    """
    Cette fonction permet de connaître le nombre de messages de l'utilisateur courant en fournissant l'utilisateur courant.
    Elle retourne le nombre sous forme de int ou None si le serveur est inaccessible.
    """
    def obtenir_nombre_messages(self):
        if self.socket.connect():
            self.socket.send("OBTENIR_NOMBRE_MESSAGES")
            self.socket.send(self.current_user)
            reponse = self.socket.receive()
            self.socket.disconnect()
            return reponse

    """
    Cette fonction permet de connaître le nombre d'octets que le répertoire de l'utilisateur courant utilise.
    Elle retourne le nombre sous forme de int ou None si le serveur est inaccessible.
    """
    def obtenir_taille_dossier(self):
        if self.socket.connect():
            self.socket.send("OBTENIR_TAILLE_DOSSIER")
            self.socket.send(self.current_user)
            reponse = self.socket.receive()
            self.socket.disconnect()
            return reponse
