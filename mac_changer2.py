import subprocess
import optparse

parse=optparse.OptionParser()
parse.add_option("-i","--interface",dest="interface",help="interface change")
parse.add_option("-m","--mac",dest="mac_address",help="New Mac Adress")
(entries,arguments )=parse.parse_args()
inter=entries.interface
mac_address=entries.mac_address



subprocess.call(["ifconfig", inter,"down"])
subprocess.call(["ifconfig", inter,"hw","ether",mac_address])
subprocess.call(["ifconfig",inter,"up"])
print("Mac address changed successfully")

