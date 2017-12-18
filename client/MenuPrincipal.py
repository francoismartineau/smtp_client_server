import sys
"""
Cette classe sert à afficher le menu principal du programme, une fois que l'utilisateur se connecte.
Elle peut afficher les menus MenuEnvoiCourriel, MenuConsultationCourriels et MenuStatistiques
Via la classe Requetes elle appelle:
    -get_current_user()
Une fois son activation terminée, le programme retourne au menu d'introduction.
"""
class MenuPrincipal:
    def __init__(self, client):
        self.client = client

    def activer(self):
        while True:
            self.client.clear_console()
            tabs = "\t\t\t\t\t"
            bar = "------------------------------------------"
            print("\n" + bar + "MENU PRINCIPAL" + bar + "\n\n\n\n\n\n\n")
            print(tabs + "[1] Envoi de courriels")
            print(tabs + "[2] Consultation de courriels")
            print(tabs + "[3] Statistiques")
            print(tabs + "[4] Quitter")
            while True:
                choix = input(tabs)
                if choix == "1":
                    self.client.activer_menu_envoi_courriel()
                    break
                elif choix == "2":
                    self.client.activer_menu_consultation_courriels()
                    break
                elif choix == "3":
                    self.client.activer_menu_statistiques()
                    break
                elif choix == "4":
                    self.__quitter()
                    return
                else:
                    print("Veuillez entrer un chiffre entre 1 et 4 inclusivement.")
        
    """
    Cette fonction permet de revenir au menu d'introduction.
    """
    def __quitter(self):
        self.client.clear_console()
        print("\n\n\n\n\n\n\n\n\t\t\t\t\t\tAurevoir " + self.client.req.get_current_user().split('@reseauglo.ca')[0] + '!')
        self.client.wait(2)
