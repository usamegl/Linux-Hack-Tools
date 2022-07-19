#!/usr/bin/env python
import os
import py_compile
os.system("apt-get install figlet")
os.system("clear")
os.system("FIGLET COMPILATION TOOL")
print("""
WELCOME THE COMPILATION TOOL


""")
compilation=input("Program Name: ")
py_compile.compile(compilation)

