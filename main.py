from communication.receiver import listen_for_connection
import sys


def main():
    port = 0
    port = sys.argv[1]
    receiver.listen_for_connection(port);
    
if __name__ == '__main__':
    main()
