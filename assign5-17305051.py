import sys,os,re
'''
Name: Mohammad Syed
Student Number : 17305051
Email : mohammad.syed@ucdconnect.ie
course : Electronic Engineering

the code is as follows, system arguments 
-n : Will print number of unique ip addresses in log file
-t : will print top N IP addresses in the log file
-v : number of visits by an ip address
-L : lists all requests made by an IP address
-d : number of requests on a specific date
'''
from collections import Counter
import calendar,datetime,time


file = sys.argv[1]
argument = sys.argv[2]



def ip_address_extractor(file):
   ip_list = []
   req_list = []
   ie = re.compile(r'^(?P<ip>(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])) - -')
   with open(file) as f:
      for l in f:
        m = ie.match(l)
        if m is not None:
            ip = m.groupdict()['ip']
            ip_list.append(ip)
   return ip_list


def feature1(file):
   ip_list = ip_address_extractor(file)
   cr = len(set(ip_list))
   print(cr)


def feature2(file,requests):
   ip_list = ip_address_extractor(file)
   y = Counter(ip_list).most_common(requests)
   print("IP\t\tREQUESTS")
   for xs in y:
        print('\t'.join(map(str, xs)))

def feature3(file,ip):
   visit = 0
   f = open(file,"r")
   x = []
   times = []
   for line in f:
      parts = line.split(" - - ")
      if parts[0] == ip:
         time_v = parts[1].split(" ")[0][1:]
         times.append(calendar.timegm(time.strptime(time_v,'%d/%b/%Y:%H:%M:%S')))
   for i in range(len(times)):
      if times[i]-times[i-1]>3600:
         visit+=1
   print(visit)

def feature4(file,ip):
   x = open(file,"r")
   for line in x:
      if (line.split(" - - ")[0]) == ip:
         print(line)

def feature5(file,date):
   d = []
   a = open(file,"r")
   for line in a:
      w = line.split("]")[0].split("[")[1].split(":")[0] 
      if (w.replace("/","",len(w)) == date):
         d.append(line.split(" - - ")[0])

   y = Counter(d).most_common()
   print("IP\t\tREQUESTS")
   for xs in y:
       print('\t'.join(map(str, xs)))

if argument == "-n":

   feature1(file)

elif argument == "-t":
   requests = int(sys.argv[3])
   feature2(file,requests)

elif argument == "-v":
   ip_address = sys.argv[3]
   feature3(file,ip_address)
   
elif argument == "-L":
   ip_address = sys.argv[3]
   feature4(file,ip_address)

elif argument == "-d":
   date = sys.argv[3]
   feature5(file,date)

else:
   print("Invalid Option")




   
