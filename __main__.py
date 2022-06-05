from sys import argv, exit

CONNECTED_CLIENTS = dict()
CONNECTED_SERVERS = dict()
ROOM_ASSOCIATION = dict()

def main(args: list[str]):
    host, port = args
    port = int(port)

if __name__ == "__main__":
    exit(main(argv[1:]))

"""
1. Connect to preexisting server
2. Request server data (inc. id)
   Request room association data
3. Introduce self to servers
4. Handle connecting clients
"""