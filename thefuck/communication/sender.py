from socket import *
import pickle

def send_to_client( corrected_commands, connection_socket):
    # connectionSocket.send(str(len(correctedCommands)))
    # for items in correctedCommands:
    #     connectionSocket.send(pickle.dumps(items))
    connection_socket.send(pickle.dumps(corrected_commands))
    connection_socket.close()
