import corrector
from .sender import send_to_client

def receive_command(command, connection_socket):
    corrected_commands = corrector.get_corrected_commands(command)
    if corrected_commands == None:
        print("Sending none")
        send_to_client(None, connection_socket)
        
    print("Sending off")
    packaged_corrected_commands = []
    for command in corrected_commands:
        print(command.script)
        if command.side_effect == None:
            packaged_corrected_commands.append((command.script, # script 
                                              None, # side_effect
                                              command.priority)) # priority

        else:
            packaged_corrected_commands.append((command.script, # script 
                                                command.side_effect[0].script, # side_effect
                                                command.side_effect[0].stdout,
                                                command.side_effect[0].stderr,
                                                command.side_effect[1],
                                                command.priority)) # priority

    send_to_client(packaged_corrected_commands, connection_socket)
