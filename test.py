import os
from scapy.all import *

# found this on http://hackoftheday.securitytube.net/2013/03/wi-fi-sniffer-in-10-lines-of-python.html
ap_list = []
def PacketHandler(pkt):
    if pkt.haslayer(Dot11):
        if pkt.type == 0 and pkt.subtype == 8:
            if pkt.addr2 not in ap_list:
                ap_list.append(pkt.addr2)
                print "AP MAC: %s with SSID: %s " %(pkt.addr2, pkt.info)

interface = raw_input("Enter name of monitor interface: ")
os.system('cls' if os.name == 'nt' else 'clear')
sniff(iface=interface, prn = PacketHandler )
