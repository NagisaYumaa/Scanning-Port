import socket
import datetime
from datetime import datetime
import sys

target = input('Enter the host to be scanned: ')

def port_scan(target):
    try:
        ip= socket.gethostbyname(target)
        print(f"Scanning {ip} ....")
        print ("Time started:" + str(datetime.now()))
        for portt in range(10, 3307):
            # //print(f"Scanning port {portt} ....")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(.1)
            result = sock.connect_ex((ip, portt))
            if result == 0:
                print(f"Port {portt}: Open")
            sock.close()
    
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

port_scan(target)
