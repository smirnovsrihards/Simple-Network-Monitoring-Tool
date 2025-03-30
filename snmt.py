#!/usr/bin/env python3

import socket
from concurrent.futures import ThreadPoolExecutor
from scapy.all import *
import ipaddress
import cmd
import pyfiglet

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

        result = srp(packet, timeout=3, verbose=0)[0]

        hosts=[]
        
        for sent, received in result:
            hosts.append({'ip': received.psrc, 'mac': received.hwsrc})
        print("Active hosts in the network:")
        print("IP" + " "*18+"MAC" )
        for host in hosts:
            print("{:16}   {}".format(host['ip'], host['mac']))

class ICMPScan:

    def __init__(self, target):
        self.target = target

    def ping(self, target):
        
        print(f"Scanning network: {target}")
        active_hosts = []
        
        net = ipaddress.IPv4Network(target, strict=False)

        for ip in net.hosts():
            response = sr1(IP(dst=str(ip))/ICMP(), verbose=0, timeout=1)
            
            if response:
                print(f'Host {ip} is active')
                active_hosts.append(str(ip))
                break

class PortScan:
    def __init__(self, target):
        self.target = target
    
    def tcp_scan(self, target, port):
        packet = IP(dst=target)/TCP(dport=port, flags='S')
        response = sr1(packet, timeout=1, verbose=0)
        if response[TCP].flags == "SA":
            print(f"Port {port} is open.")
    
    def udp_scan(self, target, port):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock_udp:
            sock_udp.settimeout(1)
            try:
                sock_udp.sendto(b'www.google.com', (target, port))
                data, _ = sock_udp.recvfrom(1024)
                print(f"Port: {port} is open!")
            except socket.timeout:
                print(f"Port: {port} is open | filtered!")
            except socket.error as e:
                print(f"Port: {port} is closed or unreachable: {e}")
            

    def run_scan(self, first_port, last_port, scan_protocol):
        ports = range(first_port, last_port + 1)
        
        if scan_protocol == 'TCP':
            with ThreadPoolExecutor(max_workers=10) as executor:
                executor.map(lambda port: self.tcp_scan(self.target, port), ports)
        else:
            with ThreadPoolExecutor(max_workers=10) as executor:
                executor.map(lambda port: self.udp_scan(self.target, port), ports)

class TCPSniffer:
    pass

class UDPSniffer:
    pass

class MyShell(cmd.Cmd):
    
    prompt = '>_ '
    
    def __init__(self, target):
        super().__init__()
        self.arpscan = ARPScan(target)
        self.icmpscan = ICMPScan(target)
        self.portscan = PortScan(target)
   
    def do_arpscan(self, arg):
        print(self.arpscan.find(target))

    def do_icmpscan(self, arg):
        print(self.icmpscan.ping(target))

    def do_portscan(self, arg):
        first_port = int(input("Please input first port: "))
        last_port = int(input("Please input last port: "))
        scan_protocol = input("Please Select Scan Protocol: TCP or UDP: ")
        print(self.portscan.run_scan(first_port, last_port, scan_protocol))

    def do_exit(self, arg):
        print("Exiting CLI...")
        return True

if __name__ == '__main__':
   
    ascii_banner = pyfiglet.figlet_format("Network Monitor")
    print(ascii_banner)
    
    target = input("Please input IP address or network: ")   

    cli = MyShell(target)
    cli.cmdloop()
