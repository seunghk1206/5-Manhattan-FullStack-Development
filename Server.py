import socket
from _thread import *
import sys

server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#bridge

try: #에러가 일어났을때 체크하기위한 코드
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2) # unlimited player can join this game, but if 2, only 2 can enter
print("Waiting for a connection...")
print("server started!")

def threaded_client(conn):
    conn.send(str.encode("connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048) # 2^11 만큼의 데이터를 먼저 받는다 -> encode
            reply = data.decode("utf-8") # 사람의 언어로 바꿔줘야된다 -> decode
            if not data:
                print("Disconnected")
                break
            else:
                print("Recieved:", reply)
                print("Sending:", reply)

            conn.sendall(str.encode(reply)) #encode 해서 보내고 decode 해서 받는다
        except:
            break

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, ))