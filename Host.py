import socket
import time
class Host:

    @staticmethod
    def modify_array(array, array2, players):
        for i in range(0, players, 1):
            if array2[i][2] == array.split(" ")[2]:
                array2[i] = array.split(" ")
                print("Adding split array (player = " + array.split(" ")[2] + ") : " + str(array.split(" ")), end="")

    @staticmethod
    def send_data():
        master_map_data = [["0","0","0"],["0","0","1"],["0","0","2"],["0","0","3"]]
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('localhost', 5000))
        while True:
            data, addr = sock.recvfrom(1024)
            if not data:
                break
            print(str(addr) + " sent this: " + data.decode("utf-8"))
            Host.modify_array(data.decode("utf-8"), master_map_data, 4)
            print("\nGave: " + str(master_map_data))
            sock.sendto(str.encode(str(master_map_data)), addr)
            time.sleep(.02)
        sock.close()
Host.send_data()