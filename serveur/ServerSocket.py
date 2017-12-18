import struct, pickle, socket
"""
Cette classe sert à établir la communication au serveur à permettre les demandes de connexions d'éventuels clients.
Elle utilise un socket.
Elle traduit les variables python en octets et vice versa via le module pickle.
"""
class ServerSocket:

    """
    Initialisation d'un socket.
    """
    def __init__(self, address, port, monitor_exchanges = True): 
        self.address = address
        self.port = port
        self.monitor_exchanges = monitor_exchanges
        self.connection_counter = 0
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.address, self.port)) 
        self.socket.listen(5)
        print("Serveur actif: " + self.address + ", " + str(self.port))
    
    """
    Connexion à la demande d'un client.
    """
    def accept_client(self):
        self.connection_counter += 1
        (self.client_socket, (client_address, client_port)) = self.socket.accept()
        if self.monitor_exchanges:
            console_separator = " --------------------------------------------------------------"
        else:
            console_separator = ""
        message = "\nConnection #" + str(self.connection_counter) + ": " + client_address + console_separator
        print(message)
    
    """
    Déconnexion du socket qui doit idéalement être synchronisée avec le client.
    """
    def leave_client(self):
        self.client_socket.close()
    
    
    """
    Réceptions d'octets et traduction en variable python.
    La méthode reçoit le format du message (un int qui prend 4 octets) et ensuite peut recevoir le message.
    """
    def receive(self):
        try:
            length, = struct.unpack("!I", self.recvall(4))
            msg = pickle.loads(self.recvall(length))
            if self.monitor_exchanges:
                print("\t->  " + repr(str(msg)))
            return msg
        except socket.error:
            print("\tLe client est inaccessible.")
    

    """
    Traduction d'une variable python en octets en envoi vers le serveur.
    La méthode envoie la taille du message et ensuite le message.
    """
    def send(self, msg):
        try:
            if self.monitor_exchanges:
                print("\t<-  " + repr(str(msg)))
            msg = pickle.dumps(msg)
            length = struct.pack("!I", len(msg))
            self.client_socket.sendall(length)
            self.client_socket.sendall(msg)
        except socket.error:
            print("\tLe client est inaccessible.")
    

    """
    Cette méthode permet de recevoir un message d'un nombre d'octets donné en paramètre.
    """
    def recvall(self, count):
        buf = b""
        while count > 0:
            newbuf = self.client_socket.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf
