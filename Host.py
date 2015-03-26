import socket
import time
class Host:
    def __init__(self, IP_V4, max_players):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((IP_V4, 5000))
        self.max_players = max_players
        self.start = False
        self.clients = []

    @staticmethod
    def modify_array(array, array2, players):
        for i in range(0, players, 1):
            if array2[i][2] == array.split(" ")[2]:
                array2[i] = array.split(" ")

    def send_data(self):
        self.start = True
        master_map_data = [["0","0","0"],["0","0","1"],["0","0","2"],["0","0","3"]]
        while True:
            data, addr = self.sock.recvfrom(1024)
            if not data:
                break
            Host.modify_array(data.decode("utf-8"), master_map_data, self.max_players)
            self.sock.sendto(str.encode(str(master_map_data)), addr)
            time.sleep(.02)
        self.sock.close()

    def close_socket(self):
        self.sock.close()

    def get_clients(self):
        for i in range(0, self.max_players, 1):
            try:
                data, addr = self.sock.recvfrom(1024)
                if addr not in self.clients:
                    self.clients.append(addr)
            finally:
                pass

        return self.clients



print("Hello, Welcome to the server!")
players = int(input("Firstly how many players? "))
print("Ok, server initialized")
host = Host('192.168.1.5', players)
inpt = input("Start Server (y for yes)")
while inpt != 'y':
    print("__________________________")
    print("Ok Here are your options: ")
    print("__________________________")
    print("Change Map             (1)")
    print("List connected players (2)")
    inpt = input("Selection: ")
    if inpt == "2":
        print(host.get_clients())
        print("All clients printed")
    inpt = input("Start Server (y for yes)")

host.send_data()
