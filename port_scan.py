import socket # module for connections
import ipaddress # module for validating IP addresses
from colorama import init, Fore # module for colored text

init() #initialize colorama
GREEN = Fore.GREEN # Print in green if port is open
GRAY = Fore.LIGHTBLACK_EX # Print in gray if port is closed
RESET = Fore.RESET # Reset to default color

def is_port_open(host, port):
    #Check if a specific port is open on a given host
    #creates a new socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.AF_INET & socket.SOCK_STREAM = Use IPv4 TCP socket
    # if target slow or unresponsive, give up after 1 sec
    s.settimeout(1)
    try:
        # tries to connect to the specified host using that port
        s.connect((host, port))
    except:
        # cannot connect to the port; port is closed
        return False
    else:
        # connection successful; port is open
        return True
    finally:
        # closes socket after connection attempt
        s.close()

# get ip or hostname from user input
host = input("Enter the host IP address or domain name to scan: ")
num_ports = int(input("Enter number of ports to scan (large number ==> scan takes more time..)"))
ip = socket.gethostbyname(host) # also accept IPs (user can also enter a valid IP; method will return it)

try:
    # Validate the host input and check if it's a valid IP address
    ipaddress.ip_address(ip) 
except ValueError:
    print(f"{GRAY}[-] Invalid IP address{RESET}")
    exit()

# iterate through ports 1 to 1024
for port in range(1, num_ports):
    if is_port_open(host, port):
        # Print open ports in green
        print(f"{GREEN}[+] Port {port} is open!      {RESET}")
        portCount = portCount + 1
    else:
        # Print closed ports in gray and overwrite the line for better readability
        print(f"{GRAY}[-] Port {port} is closed..     {RESET}", end='\r')
# prints message and count after scan 
print(f"{GREEN}[+++] Completed port scan!", end="\n")
print(f"{GREEN}[+++] Ports scanned: {num_ports}", end="\n")
print(f"{GREEN}[+++] {portCount} ports are open on {host}.")  
