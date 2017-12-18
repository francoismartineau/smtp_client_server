"""
Cette classe sert à afficher le menu d'affichage de statistiques de l'utilisateur.
Via la classe Requetes, elle appelle:
    -obtenir_nombre_messages()
    -obtenir_taille_dossier()
    -consulter_liste_courriels()
Une fois son activation terminée, le programme retourne au menu principal.
"""
class MenuStatistiques:
    def __init__(self, client):
        self.client = client

    def activer(self):
        self.client.clear_console()
        print("Nombre de messages: " + str(self.obtenir_nombre_messages()))
        print("Espace utilisé: " + self.obtenir_taille_dossier())
        print("Messages:\n" + self.client.req.consulter_liste_courriels())
        input()

    def obtenir_nombre_messages(self):
        nombre = self.client.req.obtenir_nombre_messages()
        if nombre == None:
            nombre = '?'
        return nombre

    def obtenir_taille_dossier(self):
        taille = self.client.req.obtenir_taille_dossier()
        if taille == None:
            taille = '?'
        elif taille > 100:
            taille /= 1000
            taille = str(taille) + " Ko"
        else:
            taille = str(taille) + " octets"
        return taille
