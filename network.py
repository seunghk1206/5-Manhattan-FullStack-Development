import socket
import pickle

class network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ""
        self.port = 5555
        self.addr = (self.server, self.port) #ip 주소, 포트 --> 튜플
        self.p = self.connect() # id = connect를 통한 return 값

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr) #
            return pickle.loads(self.client.recv(10000))
        except:
            pass

    def send(self, data):
        try: 
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(10000))
        except socket.error as e:
            print(e)
