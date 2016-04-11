from socket import *
from communication import client_facade
from communication import sender
from thefucktypes import Command
import pickle

def listen_for_connection(port):
    server_port = port
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)
    print ('The Server is ready to receive')
    while 1:
        connection_socket, addr = server_socket.accept()
        command = pickle.loads(connection_socket.recv(1024))
        command = Command(command[0], command[1], command[2])
        print("received " + command.script)
        send_for_correction(command, connection_socket)
        # send_back(command, connection_socket)


def send_for_correction(command, connection_socket):
    client_facade.receive_command(command, connection_socket)

def send_back(command, connection_socket):
    sender.send_to_client(command, connection_socket)

