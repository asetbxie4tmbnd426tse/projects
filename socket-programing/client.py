import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MASSAGE = "!DISCONNECT"
SERVER = "10.0.0.4"
ADDR = (SERVER, PORT)

connected = False

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

def recive_protocol():
    while connected:
        message_length = client.recv(HEADER).decode(FORMAT)
        if message_length:
            message_length = int(message)
            message = client.recv(message_length).decode(FORMAT)
            print(message)
            client.send("Message received".encode(FORMAT))

def handle_server():
    recive_protocol()
    client.close()
    pass

def start_client():
    connected = True
    thread = threading.Thread(target=handle_server)
    thread.start()
    while connected:
        message = input()
        if message == DISCONNECT_MASSAGE:
                connected = False
        send_protocol(message)
    pass

welcom_message = "Hello and wellcom to the message room. This message room is in your local network. That means every one who is connected to your wifi or wirely can enter the room."
disconnection = f"In order to disconnect right: {DISCONNECT_MASSAGE}"

print(f"{welcom_message} {disconnection}")
start_client()