#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet MAC CHANGER")
print("""
WELCOME THE MAC CHANGER TOOL
1)RANDOM MAC
2)MANUAL MAC
3)MAKE MAC ADRESS ORIGINAL

""")
process_no=input("Enter the process no: ")
if(process_no=="1"):
	os.system("ifconfig eth down")
	os.system("macchanger -r eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mNEW MAC ADRESS RANDOM DETERMINED")
elif(process_no=="2"):
	macaddress=input("Enter the NEW MAC ADDRESS: ")
	os.system("ifconfig eth down")
	os.system("macchanger --mac " +macaddress+ " eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mNEW MAC ADRESS MANUEL DETERMINED")
elif(process_no=="3"):
	os.system("ifconfig eth down")
	os.system("macchanger -p eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mNEW MAC ADRESS ORIGINAL DETERMINED")	
	
else:
	print("Invalid Process No, System  Will Be Restarting...")
