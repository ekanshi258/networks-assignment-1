import nmap
import datetime
import argparse

parser = argparse.ArgumentParser(description='Track number of hosts online on LAN')
parser.add_argument('subnet', metavar = 'PORT', type=int, help='subnet to probe')
parser.add_argument('freq', help='probing frequency per hour')
args = parser.parse_args()

subnet = args.subnet
freq = args.freq

nm = nmap.PortScanner()     #instantiate nmap port scanner object

#print(nm.csv())