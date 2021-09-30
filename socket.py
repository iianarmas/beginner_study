# Connecting to a target host

from socket import *
import socket
import sys

if __name__ == "__main__":
    try:
        sock = socket.socket(AF_INET, SOCK_STREAM)
    except socket.error as err:
        print('Failed to create a socket')
        print(f'Reason: {str(err)}')

        sys.exit()

    print('Socket created')
    
    target_host = input('Enter the target host name to connect: ')
    target_port = input('Enter the target port: ')

    try:
        sock.connect((target_host, int(target_port)))
        print(f'Socket connected to {target_host} at port {target_port}')
        sock.shutdown(2)
    except socket.error as err:
        print(f'Failed to connect to {target_host} at port {target_port}')
        print(f'Reason: {str(err)}')
        sys.exit()
        
# ====================================================
