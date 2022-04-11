#!/usr/bin/python3
import socket
import os
from psutil import process_iter
from signal import SIGTERM

# check for open ports
def portScan():
    #ip = input('Enter a scan target: ')
    ip = '127.0.0.1'
    for port in range(0, 65536):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # specific to this device
        #result = sock.connect_ex(('127.0.0.1', port))
        result = sock.connect_ex((ip, port))

        # if port is open
        if (result == 0):
            # check if port is using protocol
            try:
                protocol = socket.getservbyport(i)
                print(f'Port {port} is open using {protocol} protocol')
            except:
                print(f'Port {port} is open using no protocol')
        sock.close()

# kill processes
def procKill():
    for proc in process_iter():
        try: 
            for conn in proc.connections():
                print(f'Killing RDP process on port {conn.laddr.port}')
                #proc.send_signal(SIGTERM)
                os.system(f'lsof -i :{conn.laddr.port}')
        except:
            print(proc)

def closePort():
    print('Not yet implemented')
        
def main():
    while True:
        userIn = int(input('Enter a number:\n1) Scan Ports\n2) Kill Processes\n3) Close Ports\n4) Exit\n'))
        if (userIn == 1):
            portScan()
        elif (userIn == 2):
            procKill()
        elif (userIn == 3):
            closePort()
        elif (userIn == 4):
            return
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()
