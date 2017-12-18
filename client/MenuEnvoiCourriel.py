"""
Cette classe sert à afficher le menu d'envoi de courriels
Via la classe Requetes elle appelle:
    -envoyer_courriel()
Une fois son activation terminée, le programme retourne au menu principal.
"""

class MenuEnvoiCourriel:
    def __init__(self, client):
        self.client = client

    def activer(self):
        self.client.clear_console()
        adresse = input("| Destinataire | ")
        sujet =   input("| Sujet        | ")
        print("------------------------------------------------------------")
        print("Vous pouvez écrire votre message.\n")
        print('Pour l\'envoyer, écrivez "envoyer" sur une nouvelle ligne.')
        print('Pour quitter, écrivez "quitter" sur une nouvelle ligne.\n')
        print("------------------------------------------------------------")
        # détecter backspace ?
        message = ""
        while True:
            line = input()
            if line == "envoyer":
                break
            elif line == "quitter":
                return
            else:
                message += line + '\n'
    
        if self.client.req.envoyer_courriel(adresse, sujet, message):
            print("Le message a été envoyé.")
        else:
            print("Le message n'a pas pu être envoyé, veuillez réessayer ultérieurement.")
        input()
