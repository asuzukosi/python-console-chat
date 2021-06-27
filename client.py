import socket
import threading
import time

PORT = 5051
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)
FORMAT = 'utf-8'
START_COMMAND = "--start--"

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
client.connect(ADDR)

def send():
    print("You can now type in your messages...")
    while True:
        message = input()
        if message.find("|") == -1 :
            print("Invalid message format \n")
            print("The format is : name | message \n")
            print("If you wish to send it to everyone specify the name as 'all' \n")
            continue
        client.send(message.encode(FORMAT))

def receive():
    while True:
        message = client.recv(2056).decode(FORMAT)
        if message == START_COMMAND:
            username = input("Enter your username: ")
            client.send(username.encode(FORMAT))
        else:
            print(message, "\n")


sending_thread = threading.Thread(target=send)
receiving_thread = threading.Thread(target=receive)

receiving_thread.start()
time.sleep(10)
sending_thread.start()
