#!/usr/bin/python3

# Fetching the weather

from requests import get
import json
from pprint import pprint
import re
from urllib2 import urlopen

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)
city = data['city']
country=data['country']
region=data['region']


url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22" + city + "%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

stations = get(url).json()['query']

print(stations)