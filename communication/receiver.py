from socket import socket
from .clientFacade import receive_command


def listen_for_connection(port):
    serverPort = port
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)
    print ('The Server is ready to receive')
    while 1:
        connection_socket, addr = server_socket.accept()
        command - connection_socket.recv(1024)
        send_for_correction(command, connection_socket)

def send_for_correction(command, connection_socket):
    receive_command(command, connection_socket)
