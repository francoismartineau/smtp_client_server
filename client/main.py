import optparse, sys
from Client import Client
from Socket import Socket


"""
This file is the program's entry point.
Its parameters are:
    -a --address followed by the servers's IP address. This parameter must be specified.
    -p --port followed by the server's port. Default is 1337 for both client and server.
    -h --help displays this message.
"""
parser = optparse.OptionParser()
parser.add_option("-a", "--address", action = "store", dest = "address", help = "This option is obligatory and must be equivalent to the server's IP address.")
parser.add_option("-p", "--port", action = "store", dest = "port", default = 1337, type = int, help = "This option's value must correspond to the server's port. By default, it's 1337 for both client and server.")
opts = parser.parse_args(sys.argv[1:])[0]



if opts.address == None:
    print("Use -h --help to get help.")
else:
    interface_utilisateur = Client(Socket(opts.address, opts.port))
