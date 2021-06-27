import socket
import threading
import time

PORT = 5051
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)
START_COMMAND = "--start--"
FORMAT = "utf-8"

active_connections = []

# set up server
server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.bind(ADDR)


# set up database
temp_db = dict()

def handle_client(conn, addr):
    connected = True
    # request user to register
    conn.send(START_COMMAND.encode(FORMAT))
    time.sleep(2)
    username = conn.recv(2056).decode(FORMAT)
    temp_db[addr] = username


    # introduce user to group
    conn.send("Welcome to python console chat".encode(FORMAT))
    num_active = len(active_connections)
    if num_active > 0:
        time.sleep(2)
        conn.send(f"There are {num_active} active users, and they are: ".encode(FORMAT))
        for connection in active_connections:
            conn.send(f"IP address: {connection[1]} as {temp_db[connection[1]]}".encode(FORMAT))
    
    while True:
        message:str = conn.recv(2056).decode(FORMAT)
        if message.find("|") == -1:
            conn.send("Invalid message format".encode(FORMAT))
        print(message)
        name, message = message.split('|')
        
        name = name.strip()
        if name == "all":
            for connection in active_connections:
                        connection[0].send(f"{username} sent everybody: {message}".encode(FORMAT))
        for k, v in temp_db.items():
            if v == name:
                
                for connection in active_connections:
                    if k == connection[1]:
                    
                        connection[0].send(f"{username} sent you: {message}".encode(FORMAT))

        



def start_server():
    server.listen()
    while True:
        
        conn, addr = server.accept()
        handler = threading.Thread(target=handle_client, args=(conn, addr))
        handler.start()
        active_connections.append((conn, addr))
        print("New connection with", addr)
        print("Number of active connections is : ", threading.active_count() - 1)


if __name__ == '__main__':
    print("SEVER HAS STARTED AT :", ADDR)
    start_server()