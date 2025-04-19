#!/usr/bin/env python3
from core.database import SQLDatabase
from core.configer import ConfManager 
from core.scanner import Scanner
from core.ping import ICMPScan
import pyfiglet
from colorama import Fore, init

def main():
    init(autoreset=True)
    
    read = ConfManager
    config_data = read.read_config()
    
    subnet = config_data['subnet']
    port_range = config_data['port_range']
    db_name = config_data['db_name']
    
    SQLDatabase(db_name)

    scanner = Scanner(subnet, port_range, db_name)
    hosts = scanner.scan()
    
    if not hosts:
        print(f"{Fore.YELLOW}[-] No hosts alive. Exiting...")
        print("")
        return

    watch = ICMPScan(hosts)
    watch.ping_host()
    
if __name__ == "__main__":
    ascii_banner = pyfiglet.figlet_format("Network Monitor")
    print(Fore.MAGENTA, ascii_banner)
    main()
