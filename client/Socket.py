import struct, pickle, socket
from Requetes import Requetes

"""
Cette classe sert à établir la connexion entre le client et le serveur.
Elle utilise un socket.
Elle traduit les variables python en octets et vice versa via le module pickle.
"""
class Socket:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port

    """
    Initialisation d'un socket.
    """
    def connect(self):
        succes = True
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.server_address, self.server_port))
        except:
            print("Le serveur est indisponible.")
            succes = False
        return succes
            
    """
    Déconnexion du socket qui doit idéalement être synchronisée avec le serveur.
    """
    def disconnect(self):
        self.socket.close()

    def receive(self):
        try:
            length, = struct.unpack("!I", self.__recvall(4))
            msg = pickle.loads(self.__recvall(length))
        except:
            print("Le serveur est inaccessible.")
            msg = None
        return msg
    
    """
    Traduction d'une variable python en octets en envoi vers le serveur.
    La méthode envoie la taille du message et ensuite le message.
    """
    def send(self, msg):
        try:
            msg = pickle.dumps(msg)
            length = struct.pack("!I", len(msg))
            self.socket.sendall(length)
            self.socket.sendall(msg)
        except:
            print("Le serveur est inaccessible.")
    
    """
    Cette méthode permet de recevoir un message d'un nombre d'octets donné en paramètre.
    """
    def __recvall(self, count):
        buf = b""
        while count > 0:
            newbuf = self.socket.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf










