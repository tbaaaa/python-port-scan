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