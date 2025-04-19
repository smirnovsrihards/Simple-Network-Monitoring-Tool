import nmap
from colorama import Fore, init
from core.notifier import SendMail
import time

class ICMPScan:
    def __init__(self, hosts):
        self.hosts = hosts
    
    def ping_host(self):
        init(autoreset=True)
        monitoring = True
        scanner = nmap.PortScanner()
        nmap_arg = '-sn'

        try:
            while monitoring:
                for host in self.hosts:
                    time.sleep(1)
                    try:
                        scanner.scan(host, arguments=nmap_arg)
                        print(f"{Fore.GREEN}[+] {host} is {scanner[host].state()}!")
                    except Exception as e: 
                        print(f"{Fore.RED}[-] {e} is down!")
                        print(f"{Fore.YELLOW}[-] Sending Alert...")
                        notify = SendMail(host)
                        notify.send()
                        self.hosts.remove(host)
                        time.sleep(1)
        except KeyboardInterrupt:
            print(f"{Fore.YELLOW} [-] Exiting...")
