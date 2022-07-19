#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("FIGLET VPN CONTROL")
print("""
WELCOME THE VPN CONTROL TOOL

""")
target_ip=input("Target IP: ")
os.system("ike-scan " +target_ip)
