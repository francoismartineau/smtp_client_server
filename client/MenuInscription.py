import re
"""
Cette classe sert à afficher le menu d'inscription
Via la classe Requetes elle appelle:
    -inscrire_utilisateur()
    -utilisateur_existe()
    -password_validity()
Une fois son activation terminée, le programme retourne au menu d'introduction.
"""
class MenuInscription:
    def __init__(self, client):
        self.client = client

    def activer(self):
        tabs = "\t\t\t"
        print(tabs + "-> INSCRIPTION\n")
        print(tabs + "Un nom d'utilisateur valide doit contenir au moins\n" + tabs + "un caractère, suivi de @reseauglo.ca\n" + tabs + "Un mot de passe valide doit:\n" + tabs + "- comporter de 6 à 12 caractères,\n" + tabs + "- être composé d'au moins une lettre et un chiffre\n\n")
        self.__set_username()
        self.__set_password()
        if self.client.req.inscrire_utilisateur(self.username, self.password):
            print(tabs + "L'inscription a réussi.")
        else:
            print(tabs + "Un problème s'est produit. Veuillez réessayer ultérieurement.")
        self.client.wait(3)
    
    
    
    def __set_username(self):
        tabs = "\t\t\t"
        while True:
            username = input(tabs + "Nom d'utilisateur:")
            if not MenuInscription.__nom_valide(username):
                print(tabs + "Assurez vous que le nom d'utilisateur choisit est valide.")
            elif self.client.req.utilisateur_existe(username):
                print(tabs+ "Le nom choisi existe déjà. Veuillez en choisir un autre.")
            else:
                self.username = username
                break
    
    @staticmethod
    def __nom_valide(nom):
        return bool(re.search(r"^.+@reseauglo.ca", nom))
    
    
    def __set_password(self):
        tabs = "\t\t\t"
        while True:
            password = self.client.private_input(tabs + "Mot de passe: ")
            if self.client.req.password_validity(password):
                if self.__confirm_password(password):
                    self.password = password
                    break
            else:
                print(tabs + "Le mot de passe ne respecte pas les critères de validité.")


    def __confirm_password(self, password):
        tabs = "\t\t\t"
        confirmation = False
        password2 = self.client.private_input(tabs + "Confirmer mot de passe: ")
        if password == password2:
            confirmation = True
        else:
            print(tabs + "Assurez vous d'entrer le même mot de passe les deux fois.")
        return confirmation



