import socket #module for connections
from colorama import init, Fore #module for colored text

init() #initialize colorama
GREEN = Fore.GREEN #Print in green if port is open
GRAY = Fore.LIGHTBLACK_EX #Print in gray if port is closed
RESET = Fore.RESET #Reset to default color

def is_port_open(host, port):
    """Check if a specific port is open on a given host"""
    #creates a new socket object
    s = socket.socket()
    try:
        #tries to connect to the specified host using that port
        s.connect((host, port))
        return True #if connection is successful, the port is open
    except:
        return False #if connection fails, the port is closed