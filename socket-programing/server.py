import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MASSAGE = "!DISCONNECT"
clients_list = []
message_log = []
#new_message = []

lock = threading.Lock()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def _remove_client_from_list(addr):
    try:
        for i in range(len(clients_list)):
            if clients_list[i][addr] == addr:
                del clients_list[i]
                break
    except:
        pass
def send_protocol(msg, conn):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_legth = str(msg_length).encode(FORMAT)
    send_legth += b' ' * (HEADER - len(send_legth))
    conn.send(send_legth)
    conn.send(message)

def send_to_all_clients(message):
    #sends the message to all the connected clients 
    try:
        lock.acquire()
        for client in clients_list:
                send_protocol(message, conn=client["conn"])
        lock.release()
    except IndexError:
        pass
        
def message_log_to_new_client(conn):
    try:
        lock.acquire()
        for message in message_log:
            send_protocol(message, conn=conn)
        lock.release()
    except:
        pass

def recive_protocol(conn, addr):
    connected = True
    while connected:
        message_length = conn.recv(HEADER).decode(FORMAT)
        if message_length:
            message_length = int(message_length)
            message = conn.recv(message_length).decode(FORMAT)
            if message == DISCONNECT_MASSAGE:
                connected = False
            elif message == "Message received":
                pass
            print(f"[{addr}] {message}")
            message_log.append(f"[{addr}] {message}")
            send_protocol("Message received",conn=conn)
            send_to_all_clients(message=f"[{addr}] {message}")

def handle_client(conn, addr):
    message = f"[NEW CONNECTION] {addr} connected."
    print(message)
    message_log.append(message)
    recive_protocol(conn, addr)
    conn.close()
    _remove_client_from_list(addr)

def start():
    # This is the main part of the server. The other functions should return here
    # when they finish.
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:

        conn, addr = server.accept()
        client_info = {
            "conn": conn,
            "addr": addr,
        }
        clients_list.append(client_info)
        message_log_to_new_client(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")



print("[STARTING ] server is starting...")

start()


