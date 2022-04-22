#!/usr/bin/python3
import socket
import os
#from psutil import process_iter
from signal import SIGTERM

# check for open ports
def portScan():
    try:
        print("Scanning for ssh connections...")
        connections = os.system("w | grep -v localhost | awk 'match($8,\"sshd:\"){print $3}'")
        if connections == "":
            print("No connections found")
        else:
            print(f"Connections found:\n{connections})")
    except:
        print("Error, unable to scan")

# kill processes
def procKill():
    try: 
        print(f'Killing ssh connections...')
        #os.system("w | grep -v localhost | awk 'match($3,/[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/){print $3 $6}'")
        os.system("w | grep -v localhost | awk 'match($8,\"sshd:\"){print $3}' | ss -K")
    except:
        print('Error, could not kill ssh connections')

def main():
    while True:
        userIn = int(input('Enter a number:\n1) Scan Ports\n2) Kill Processes\n3) Exit\n'))
        if (userIn == 1):
            portScan()
        elif (userIn == 2):
            procKill()
        elif (userIn == 3):
            return
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()
