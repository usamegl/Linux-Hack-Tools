#!usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WORDLIST CREATOR ")
print("""
WELCOME THE  WORDLIST CREATOR TOOL


""")
min=input("Minimum Char: ")
max=input("Maximum Char: ")
characters=input("enter the characters you want: ")
filepath=input("Enter The FilePath: ")

os.system("crunch " +min + " "  + max + " " + characters ) 

print("SUCCCESSFULL!")
