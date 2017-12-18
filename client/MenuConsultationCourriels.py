"""
Cette classe sert à afficher le menu de consultation de courriels
Via la classe Requetes elle appelle:
    -consulter_liste_courriels()
    -consulter_courriels()
Une fois son activation terminée, le programme retourne au menu principal.
"""

class MenuConsultationCourriels:
    def __init__(self, client):
        self.client = client

    def activer(self):
        self.liste = self.client.req.consulter_liste_courriels()
        if not self.liste:
            self.client.clear_console()
            input("\t\t\t\tVous n'avez aucun email à votre actif.")
        else:
            while True:
                self.afficher_liste()
                while True:
                    courriel = None
                    choix = input()
                    if choix == "":
                        return
                    elif choix.isdigit():
                        courriel = self.client.req.consulter_courriel(choix)
                    else:
                        courriel = None

                    if courriel:
                        self.client.clear_console()
                        print(courriel)
                        input()
                        self.afficher_liste()
                    else:
                        print("Entrée invalide.")

    def afficher_liste(self):
        self.client.clear_console()
        print("-----------------------------------------------------------------")
        print("Veuillez entrer un nombre correspondant au courriel à consulter.\n\n")
        print("-----------------------------------------------------------------")
        print("Boîte de courriels:")
        print(self.liste)
            
