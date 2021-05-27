import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MASSAGE = "!DISCONNECT"
SERVER = "10.0.0.4"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_protocol(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_legth = str(msg_length).encode(FORMAT)
    send_legth += b' ' * (HEADER - len(send_legth))
    client.send(send_legth)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send_protocol("Hello World1")
input()
send_protocol("Hello World2")
input()
send_protocol("Hello World3")
input()
send_protocol("Hello World4")

send_protocol(DISCONNECT_MASSAGE)