import socket
class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def get_data(self, players, mapdata):

        self.sock.sendto(str.encode(str(mapdata[0]) + " " + str(mapdata[1]) + " " + str(mapdata[2])), ('localhost', 5000))
        data, addr = self.sock.recvfrom(1024)
        if data:
            Client.interpret(players, data.decode("utf-8"))
        if not data:
            self.sock.close()

    @staticmethod
    def interpret(players, pos_array):
        counter = 0
        pos_array = pos_array.replace("]", "", len(pos_array))
        pos_array = pos_array.replace("[", "", len(pos_array))
        pos_array = pos_array.replace(",", "", len(pos_array))
        pos_array = pos_array.replace("'", "", len(pos_array))
        print("Filtered to: " + pos_array)
        arr = []
        for s in pos_array.split(" "):
            arr.append(int(s))
        print("Put into 1D array" + str(arr))
        array = [[0]* 3 for _ in range(int(len(arr) / 3))]
        for i in range(int(len(arr) / 3)):
            for j in range(3):
                array[i][j] = arr[counter]
                counter += 1
        print("Now 2D: " + str(array))
        players.update_players(array)
