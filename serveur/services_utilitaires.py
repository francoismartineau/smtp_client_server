from hashlib import sha256
import os, re, platform
"""
Ce fichier est un regroupement de fonctions utilitaires utilisées par le module Services
"""

"""
Fonction permettant de détecter si une adresse donnée peut être locale.
Elle retourne un bool signifiant si elle est locale.
"""
def is_internal_address(address):
    return bool(re.search(r"^.+@reseauglo.ca$", address))

"""
Fonction permettant de savoir si le fichier numéro existe selon une liste de fichiers donnés.
Elle retourne un bool signifiant s'il existe.
"""
def fichier_numero_un_existe(files):
    existe = False
    for f in files:
        if f.startswith("1_"):
            existe =  True
    return existe

"""
Cette fonction permet d'incrémenter les numéros de tous les fichiers contenus dans un dossier.
"""
def incrementer_numero_fichiers(dir_name):
    files = list_files(dir_name)
    for f in files[::-1]:
        if f.split("_", 1)[0].isdigit():
            numero_incremente = int(f.split("_", 1)[0]) + 1
            current_file_path = dir_name + "/" + f
            new_file_path = dir_name + "/" + str(numero_incremente) + "_" + f.split("_", 1)[1]
            os.rename(current_file_path, new_file_path)

"""
Cette fonction retourne une liste de tous les noms de fichiers d'un dossier donné en argument.
"""
def list_files(dir_path):
    files = []
    for (dir_path, dir_names, file_names) in os.walk(dir_path):
        files.extend(file_names)
        break
    return files

"""
Cette fonction permet de hasher un string donné en argument
Elle retourne le texte hashé
"""
def hash(text):
    return sha256(text.encode()).hexdigest()
   
"""
Cette fonction permet de vider la console.
Elle est multi-plateforme
"""
def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

"""
Cette fonction retourne le nom du dossier du serveur.
"""
def get_server_path():
    path = os.path.realpath(__file__)
    if platform.system() == "Windows":
        temp_path = path
        path = ""
        for i in range(len(temp_path)):
            if temp_path[i] == "\\":
                path += "/"
            else:
                path += temp_path[i]
    path = os.path.dirname(path) + "/"
    return path

if __name__ == "__main__":
    get_server_path()
