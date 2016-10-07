# Wifinder
import os

# set the wireless interface used for scanning
def get_network_interface():
    network_interface = raw_input("Name of scanning interface: ")
    os.system('clear')
    print("Using interface: {0}").format(network_interface)
