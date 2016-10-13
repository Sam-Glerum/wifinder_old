# Wifinder
import os

# set the wireless interface used for scanning
def get_network_interface():
    network_interface = raw_input("Name of scanning interface: ")
    interfaces = os.listdir('/sys/class/net')
    os.system('clear')
    if network_interface in interfaces:
        print("Using interface: {0}").format(network_interface)
    else:
        print "Wrong interface, try again"
        get_network_interface()

get_network_interface()
