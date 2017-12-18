import socket, sys, optparse
from ServerSocket import ServerSocket
from Services import Services
from services_utilitaires import clear_console

"""
Ce fichier est le point d'entrée du programme.
Ses paramètres sont:
    -a --address suivi de l'adresse IP du serveur. Par défaut, l'adresse IP du serveur dans son réseau local est utilisée.
    -p -port suivi du numéro du port que le serveur utilisera. Par défaut, le serveur et le client utilisent le port 1337.
    -h --help qui affiche un guide sur l'interface du programme principal.
"""
clear_console()
default_ip = socket.gethostbyname(socket.gethostname())
parser = optparse.OptionParser()
parser.add_option("-a", "--address", action = "store", dest = "address", default = default_ip, help = "Cette option correpond à l'adresse IP du serveur.")
parser.add_option("-p", "--port", action = "store", dest = "port", default = 1337, type = int, help = "Cette option permet de choisir un port pour le serveur. Par défaut, 1337 est utilisé.")
opts = parser.parse_args(sys.argv[1:])[0]
if opts.address == default_ip:
    print("\nPour choisir manuellement une adresse IP (localhost par exemple), référez vous à l'aide avec -h\nToutefois, vous pouvez normalement vous contenter de copier l'adresse ci-bas et de la donner à votre client.")
    print("-----------------------------------------------------------------------------------------------\n")


"""
Le début du programme principal.
"""
services = Services(ServerSocket(opts.address, opts.port))
while True:
    services.fournir()
