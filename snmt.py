#!/usr/bin/env python3

import socket
import threading
from scapy.all import Ether, ARP, TCP, UDP, ICMP, IP, srp
import argparse
import textwrap
import cmd

class ARPScan:
    def __init__(self, target):
        self.target = target
    #ARP scan function was taken from: https://thepythoncode.com/article/building-network-scanner-using-scapy    
    def find(self, target):
        #Create ARP packet
        arp = ARP(pdst=target)
        #Create Ethernet Broadcast
        ether = Ether(dst='ff:ff:ff:ff:ff:ff')
        #Stack them
        packet = ether/arp

        result = srp(packet, timeout=3)[0]

        hosts=[]
        for sent, received in result:
            hosts.append({'ip': received.psrc, 'mac': received.hwsrc})
        print("Active hosts in the network:")
        print("IP" + " "*18+"MAC" )
        for host in hosts:
            print("{:16}   {}".format(host['ip'], host['mac']))

class ICMPScan:
    pass

class TCPSniffer:
    pass

class UDPSniffer:
    pass

class Shell(cmd.Cmd):
    pass

if __name__ == '__main__':
    
    target = '192.168.88.0/24'

    run = ARPScan(target)
    run.find(target)
