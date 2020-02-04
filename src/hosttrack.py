import nmap
import datetime
import argparse
import csv

parser = argparse.ArgumentParser(description='Track number of hosts online on LAN')
parser.add_argument('subnet', metavar = 'PORT', help='subnet to probe')
args = parser.parse_args()
subnet = args.subnet

nm = nmap.PortScanner()     #instantiate nmap port scanner object
nm.scan(hosts=subnet, arguments='-n -sP')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

now = datetime.datetime.now()
# dd/mm/YY H:M:S
time = now.strftime("%d/%m/%Y %H:%M:%S")

print(time, "hosts up: ", len(hosts_list))
for host, status in hosts_list:
    print(host + ' ' + status)

#fp = open("hackingdata.csv","a")
fp = open("hostmm.csv","a")        #for Malaviya
w = csv.writer(fp)
row = [time, len(hosts_list)]
w.writerow(row)
fp.close()
