#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT SCANNING")
print("""
WELCOME TO PORT SCANNİNG TOOL :')

1)FAST SCAN
2)SERVICE AND VERSION INFORMATION
3)OPERATING SYSTEM INFORMATION


""")

process_no=input("Enter the process number: ")

if(process_no=="1"):
	target_ip=input("Enter the Target IP: ")
	os.system("nmap " + target_ip)
	
elif(process_no=="2"):
	target_ip=input("Enter the Target IP: ")
	os.system("nmap -sS -sV " + target_ip)

elif(process_no=="3"):
	target_ip=input("Enter the Target IP: ")
	os.system("nmap -0 " +target_ip)

else:
	print("Invalid Choice")
	
