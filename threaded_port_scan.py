import socket # module for connections
from colorama import init, Fore # module for colored text
import argparse
from threading import Thread, Lock
from queue import Queue

# colorama initialization and Color Constants assignment
init()
GREEN = Fore.GREEN # if port open
GRAY = Fore.LIGHTBLACK_EX # if port closed
RESET = Fore.RESET # reset to default color

# threading and queue setup
NUM_OF_THREADS = 200
q = Queue()
print_lock = Lock()

def port_scan(port):
    # Scan a port on the global variable `host`
    try:
        s = socket.socket()
        s.connect((host, port))
    except:
        with print_lock:
            print(f"{GRAY}{host:15}:{port:5} is closed {RESET}", end="\r")
    else:
        with print_lock:
            print(f"{GREEN}{host:15}:{port:5} is open {RESET}")
    finally:
        s.close()

def scan_thread():
    global q
    while True:
        # get the port number from the queue
        worker = q.get()
        #scan that port number
        port_scan(worker)
        q.task_done()