import socket
from _thread import *
from player import *
import pickle
from gameRPS import * #Game

server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection")
print("server started")

players = [Player(0, 0, 50, 50,(255, 0, 0)), Player(100, 100, 50, 50,(0, 0, 255))]

connected = set()
games = {}
idCount = 0 

def threaded_client(conn, p, gameId): # thread는 한번 실행했을때 여러가지일을 한번에 처리해주는 역할
    global idCount
    conn.send(str.encode(p))
    reply = ""

    while True:
        data = conn.recv(4096).decode() #client = user client로 부터 받은 데이터

        if gameId in games:
            game = games[gameId]
            if not data:
                break
            else:
                if data == "reset":
                    game.reset()
                elif data != "get": # != 는 not equal을 의미 함
                    game.play(p, data)
                reply = game
                conn.sendall(pickle.dumps(reply))
        else: 
            break
    print("Lost connection")
    try:    
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2 # 각 두명의 플레이어가 접속했을때, 둘을 합쳐줘라
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new Game")
    else:
        games[gameId].ready = True
        p = 1
    start_new_thread(threaded_client, (conn, p, gameId))