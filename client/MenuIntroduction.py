import sys
"""
Cette classe sert à afficher le menu d'introduction, soit le menu affiché lors du démarrage du programme.
Elle peut déclencher les menus MenuConnexion et MenuInscription.
"""
class MenuIntroduction:
    def __init__(self, client):
        self.client = client

    def activer(self):
        while True:
            self.client.clear_console()
            title = "           _____   ______   _____  ______           _    _   _____  _       ____  \n    ____  |  __ \ |  ____| / ____||  ____|    /\   | |  | | / ____|| |     / __ \ \n   / __ \ | |__) || |__   | (___  | |__      /  \  | |  | || |  __ | |    | |  | |\n  / / _` ||  _  / |  __|   \___ \ |  __|    / /\ \ | |  | || | |_ || |    | |  | |\n | | (_| || | \ \ | |____  ____) || |____  / ____ \| |__| || |__| || |____| |__| |\n  \ \__,_||_|  \_\|______||_____/ |______|/_/    \_\\____/  \_____||______|\____/ \n   \____/                                                                         "
            tabs = "\t\t\t\t"
            print(title)
            print("\n\n\n" + tabs + "[1] Se connecter\n" + tabs + "[2] Créer un compte\n" + tabs + "[3] Quitter")
            choix = input(tabs)
            if choix == "1":
                self.__animation()
                self.client.activer_menu_connexion()
            elif choix == "2":
                self.__animation()
                self.client.activer_menu_inscription()
            elif choix == "3":
                sys.exit(0)
            else:
                print("Veuillez entrer un chiffre entre 1 et 3.")

    """
    Cette fonction n'est que visuelle et sert à animer le titre avant de changer de menu.
    """
    def __animation(self):
        self.__animation_frame("----------------------------------------------------------------------------------\n    ____  |  __ \ |  ____| / ____||  ____|    /\   | |  | | / ____|| |     / __ \ \n   / __ \ | |__) || |__   | (___  | |__      /  \  | |  | || |  __ | |    | |  | |\n  / / _` ||  _  / |  __|   \___ \ |  __|    / /\ \ | |  | || | |_ || |    | |  | |\n | | (_| || | \ \ | |____  ____) || |____  / ____ \| |__| || |__| || |____| |__| |\n  \ \__,_||_|  \_\|______||_____/ |______|/_/    \_\\____/  \_____||______|\____/ \n   \____/                                                                         ")
        self.__animation_frame("                                                                                  \n----------------------------------------------------------------------------------\n   / __ \ | |__) || |__   | (___  | |__      /  \  | |  | || |  __ | |    | |  | |\n  / / _` ||  _  / |  __|   \___ \ |  __|    / /\ \ | |  | || | |_ || |    | |  | |\n | | (_| || | \ \ | |____  ____) || |____  / ____ \| |__| || |__| || |____| |__| |\n  \ \__,_||_|  \_\|______||_____/ |______|/_/    \_\\____/  \_____||______|\____/ \n   \____/                                                                         ")
        self.__animation_frame("                                                                                  \n                                                                                  \n----------------------------------------------------------------------------------\n  / / _` ||  _  / |  __|   \___ \ |  __|    / /\ \ | |  | || | |_ || |    | |  | |\n | | (_| || | \ \ | |____  ____) || |____  / ____ \| |__| || |__| || |____| |__| |\n  \ \__,_||_|  \_\|______||_____/ |______|/_/    \_\\____/  \_____||______|\____/ \n   \____/                                                                         ")
        self.__animation_frame("                                                                                  \n                                                                                  \n                                                                                  \n----------------------------------------------------------------------------------\n | | (_| || | \ \ | |____  ____) || |____  / ____ \| |__| || |__| || |____| |__| |\n  \ \__,_||_|  \_\|______||_____/ |______|/_/    \_\\____/  \_____||______|\____/ \n   \____/                                                                         ")
        self.__animation_frame("                                                                                  \n                                                                                  \n                                                                                  \n                                                                                  \n----------------------------------------------------------------------------------\n  \ \__,_||_|  \_\|______||_____/ |______|/_/    \_\\____/  \_____||______|\____/ \n   \____/                                                                         ")
        self.__animation_frame("                                                                                  \n                                                                                  \n                                                                                  \n                                                                                  \n                                                                                  \n----------------------------------------------------------------------------------\n   \____/                                                                         ")
        self.__animation_frame("                                                                                  \n                                                                                  \n                                                                                  \n                                                                                  \n                                                                                  \n                                                                                  \n----------------------------------------------------------------------------------")
    
    """
    Cette fonction permet d'afficher les frames individuelles de l'animation.
    """
    def __animation_frame(self, text):
        self.client.clear_console()
        print(text)
        self.client.wait(0.04)



