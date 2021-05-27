import socket

class Modified_Socket(socket):
    def __init__(self, connection = None, address = None) -> None:
        super().__init__()
        self.conn = connection
        self.addr = address
    