""" Wifinder """
import os
import subprocess


interfaces = os.listdir('/sys/class/net')


def list_network_interfaces():
    for interface in interfaces:
        print("Interface: " + interface)
        print("=" * 20)


def get_network_interface():
    # set the wireless interface used for scanning
    input_network_interface = input("Name of scanning interface: ").lower()
    network_interface = input_network_interface
    return network_interface
    os.system('clear')

    # check if interface exists
    if network_interface in interfaces:
        print("Using interface: {}".format(network_interface))
        return network_interface
    else:
        print("Wrong interface, try again")
        print("=" * len("Wrong interface, try again"))
        list_network_interfaces()
        get_network_interface()


def sniff_ssid():
    network_interface = get_network_interface()
    subprocess.call(['airmon-ng', {}]).format(network_interface)
    pass


list_network_interfaces()
get_network_interface()
sniff_ssid()
