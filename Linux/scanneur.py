#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
THIS PART IS NOT CODED BY CR4ZYB0T !!!
"""
import os
from terminaltables import DoubleTable
from tabulate import tabulate

import sys, traceback
from time import sleep

if not os.geteuid() == 0:
    sys.exit("""\033[1;91m\n[!] This tool must be run as root! \n\033[1;m""")

# Exit message
exit_msg = "\n[+] Shutting down ...\n"



def config0():
    global up_interface
    up_interface = open('/opt/xerosploit/tools/files/iface.txt', 'r').read()
    up_interface = up_interface.replace("\n","")
    if up_interface == "0":
        up_interface = os.popen("route | awk '/Iface/{getline; print $8}'").read()
        up_interface = up_interface.replace("\n","")

    global gateway
    gateway = open('/opt/xerosploit/tools/files/gateway.txt', 'r').read()
    gateway = gateway.replace("\n","")
    if gateway == "0":
        gateway = os.popen("ip route show | grep -i 'default via'| awk '{print $3 }'").read()
        gateway = gateway.replace("\n","")




def home():

    config0()
    n_name = os.popen('iwgetid -r').read() # Get wireless network name
    n_mac = os.popen("ip addr | grep 'state UP' -A1 | tail -n1 | awk '{print $2}' | cut -f1  -d'/'").read() # Get network mac
    n_ip = os.popen("hostname -I").read() # Local IP address
    n_host = os.popen("hostname").read() # hostname


# Show a random banner. Configured in banner.py .  

			# Print network configuration , using tabulate as table.

    table = [["IP Address","MAC Address","Gateway","Iface","Hostname"],
                ["","","","",""],
                [n_ip,n_mac.upper(),gateway,up_interface,n_host]]
    print (tabulate(table, stralign="center",tablefmt="fancy_grid",headers="firstrow"))
    print ("")



    # Print xerosploits short description , using terminaltables as table. 
    table_datas = [
        ['\033[1;36m\nInformation\n', 'XeroSploit is a penetration testing toolkit whose goal is to \nperform man in the middle attacks for testing purposes. \nIt brings various modules that allow to realise efficient attacks.\nThis tool is Powered by Bettercap and Nmap.\033[1;m']
    ]
    table = DoubleTable(table_datas)
    print(table.table)


		# Get a list of all currently connected devices , using Nmap.
def scan(): 
    config0()


    scan = os.popen("nmap " + gateway + "/24 -n -sP ").read()

    f = open('/opt/xerosploit/tools/log/scan.txt','w')
    f.write(scan)
    f.close()

    devices = os.popen(" grep report /opt/xerosploit/tools/log/scan.txt | awk '{print $5}'").read()

    devices_mac = os.popen("grep MAC /opt/xerosploit/tools/log/scan.txt | awk '{print $3}'").read() + os.popen("ip addr | grep 'state UP' -A1 | tail -n1 | awk '{print $2}' | cut -f1  -d'/'").read().upper() # get devices mac and localhost mac address

    devices_name = os.popen("grep MAC /opt/xerosploit/tools/log/scan.txt | awk '{print $4 ,S$5 $6}'").read() + "\033[1;32m(This device)\033[1;m"

    
    table_data = [
        ['IP Address', 'Mac Address', 'Manufacturer'],
        [devices, devices_mac, devices_name]
    ]
    table = DoubleTable(table_data)

    # Show devices found on your network
    print("\033[1;36m[+]═══════════[ Devices found on your network ]═══════════[+]\n\033[1;m")
    print(table.table)
    



scan()

