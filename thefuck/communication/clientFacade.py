from thefuck.corrector import get_corrected_commands
from .sender import send_to_client


def receive_command(command, connection_socket):
    corrected_commands = get_corrected_commands(command)
    send_to_client(corrected_commands, connection_socket)
