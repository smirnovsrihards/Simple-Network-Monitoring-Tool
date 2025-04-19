import nmap
from colorama import Fore, init
from core.database import SQLDatabase 

class Scanner:
    def __init__(self, subnet: str, port_range, db_name):
        self.subnet = subnet
        self.port_range = port_range
        self.db_name = db_name

    def scan(self):
        init(autoreset=True)

        scanner = nmap.PortScanner()
        db = SQLDatabase(self.db_name)
        nmap_arg = f'-T5 -Pn -sS -sV --max-retries 1 --min-rate 10000 -p{self.port_range}'
        print(f"{Fore.GREEN}[+] Initializing Network Scan {Fore.RED}<O>")
        print("")
        scanner.scan(hosts=self.subnet, arguments=nmap_arg)
        
        hosts = []

        for host in scanner.all_hosts():
            print(f'Host: {host}')
            print(f'Hostname: {scanner[host].hostname()}')
            print(f'{Fore.GREEN}State: {scanner[host].state()}')
            hostname = scanner[host].hostname()
            state = scanner[host].state()
            
            for proto in scanner[host].all_protocols():
                print(f'Protocol: {proto}')
                ports = scanner[host][proto].keys()
                for port in sorted(ports):
                    service = scanner[host][proto][port]
                    print(f'Port: {port}\tState: {service["state"]}\tService: {service.get("name", "")}')
                    db.fill_db(host, hostname, port, proto, service, state)
            hosts.append(host)
            print(f"{Fore.MAGENTA}===== # =====")
        return hosts
        db.close()
