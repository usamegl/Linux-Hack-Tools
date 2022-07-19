#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WORDPRESS SCANNING")
print("""
WELCOME THE WORDPRESS SCANNING TOOL <3
1)FAST SCAN
2)PLUGIN SCAN
3)THEME SCAN
4)MODERATOR USERNAME SCAN

""")
process_no=input("Enter the process no: ")
if(process_no=="1"):
	website=input("Enter the url:" )
	os.system("wpscan --url " + website)

elif(process_no=="2"):
	website=input("Enter the url:" )
	os.system("wpscan --url " + website + "  --enumerate p")
elif(process_no=="3"):
	website=input("Enter the url:" )
	os.system("wpscan --url " + website + "  --enumerate t")
elif(process_no=="4"):
	website=input("Enter the url:" )
	os.system("wpscan --url " + website + "  --enumerate u")
	
else:
	print("Invalid Process NO, program will be shut down...")


