import socket

class network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ""
        self.port = 5555
        self.addr = (self.server, self.port) #ip 주소, 포트 --> 튜플
        self.id = self.connect() # id = connect를 통한 return 값
        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.addr) #
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try: 
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

n = network()
print(n.send("Hello YH"))
print(n.send("confirmed"))