# Simple-Network-Monitoring-Tool
Simple monitoring script to watch a home network. 
When the script starts, it scans the network for active hosts and their services. After that, it saves information about the subnet to a database and begins pinging the discovered hosts. If a host is down, the script will send an email to your Gmail account. Then, it removes the host from the list of active hosts and continues pinging the others.

## Installation
1. Set up config.ini
2. install requirements
3. chmod +x snmt.py
4. sudo ./snmt.py
