import scapy.all as scp
import optparse


def begin():
    parse=optparse.OptionParser()
    parse.add_option("-i","--ipaddress",dest="ip_address",help="use -i or --ipaddress wrire the ip adress ")
    (user_begin,arguments)=parse.parse_args()
    if not user_begin.ip_address:
         print("Please write  a IP ADRESS")
    return user_begin.ip_address




def scan(ip):
    req_packet=scp.ARP(pdst=ip)
    stream_packet=scp.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scp.ls(scp.Ether())
    packet=stream_packet/req_packet
    (main_packet,invalid_packet)=scp.srp(packet,timeout=1)
    main_packet.summary()

#scp.ls(scp.ARP())

myip=begin()
scan(myip)
