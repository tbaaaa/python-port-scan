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

        #set a timeout for the connection attempt
        s.settimeout(1)
    except:
        # cannot connect to the port; port is closed
        return False
    else:
        # connection successful; port is open
        return True

# get host from user input
host = input("Enter the host IP address or domain name to scan: ")
# iterate through ports 1 to 1024
for port in range(1, 1025):
    if is_port_open(host, port):
        print(f"{GREEN}[+] Port {port} is open      {RESET}") # Print open ports in green 
    else:
        print(f"{GRAY}[-] Port {port} is closed     {RESET}", end='\r') # Print closed ports in gray and overwrite the line for better readability