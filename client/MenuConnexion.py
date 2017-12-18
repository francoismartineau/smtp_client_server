"""
Cette classe sert à afficher le menu connexion.
Elle peut déclencher le menu MenuPrincipal.
Via la classe Requetes, elle appelle:
    -password_matches()
    -set_current_user()
"""
class MenuConnexion:
    def __init__(self, client):
        self.client = client 

    def activer(self):
        tabs = "\t\t\t\t"
        print(tabs + "-> CONNEXION\n\n")
        while True:
            username = input(tabs + "Nom d'utilisateur: ")
            if username == 'quitter':
                return
            password = self.client.private_input(tabs + "Mot de passe: ")
            valid = self.client.req.password_matches(username, password)
            if valid == False:
                print(tabs + " Cette combinaison utilisateur - mot de passe est inexistante.\n" + tabs + " Pour quitter, donnez quitter comme nom d'utilisateur.\n" + tabs + " Sinon, vous pouvez réessayer.\n")
            elif valid == True:
                self.client.req.set_current_user(username)
                break
            elif valid == None:
                input(tabs + "Veuillez réessayer ultérieurement.")
                return None
        self.client.activer_menu_principal()
           
