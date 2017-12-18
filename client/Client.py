import platform, os, getpass, time
from Requetes import Requetes
from MenuIntroduction import MenuIntroduction
from MenuInscription import MenuInscription
from MenuConnexion import MenuConnexion
from MenuPrincipal import MenuPrincipal
from MenuEnvoiCourriel import MenuEnvoiCourriel
from MenuConsultationCourriels import MenuConsultationCourriels
from MenuStatistiques import MenuStatistiques

"""
Program's main class
"""
class Client:
    def __init__(self, socket):
        self.req = Requetes(socket)
        self.menu_introduction = MenuIntroduction(self)
        self.menu_inscription = MenuInscription(self)
        self.menu_connexion = MenuConnexion(self)
        self.menu_principal = MenuPrincipal(self)
        self.menu_envoi_courriel = MenuEnvoiCourriel(self)
        self.menu_consultation_courriels = MenuConsultationCourriels(self)
        self.menu_statistiques = MenuStatistiques(self)
        self.activer_menu_introduction()

    """
    Interface activation functions
    """
    def activer_menu_introduction(self):
        self.menu_introduction.activer()

    def activer_menu_inscription(self):
        self.menu_inscription.activer()

    def activer_menu_connexion(self):
        self.menu_connexion.activer()

    def activer_menu_principal(self):
        self.menu_principal.activer()

    def activer_menu_envoi_courriel(self):
        self.menu_envoi_courriel.activer()

    def activer_menu_consultation_courriels(self):
        self.menu_consultation_courriels.activer()

    def activer_menu_statistiques(self):
        self.menu_statistiques.activer()

    """
    Static method that clears the console. It is multi plateform.
    """
    @staticmethod
    def clear_console():
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
    """
    Static method that asks user for input but doesn't show what's being typed to the console.
    """
    @staticmethod
    def private_input(text):
        return getpass.getpass(text)
    
    """
    Static method that stops the program's execution for a given number of seconds
    """
    @staticmethod
    def wait(sec):
        time.sleep(sec)
