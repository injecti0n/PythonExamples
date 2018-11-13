#!/usr/bin/python3
from itertools import groupby
import collections


items = [76,92.3,"hello",True,4,76]

#items.append=("apple",76)
items.append("apple")
items.append(76)
items.insert(2,"cat")
items.insert(0,99)
print "'Hello' is at : " , items.index('hello')
counter=collections.Counter(items)
print "ArrayList = " , (items)
print "Counting ArrayItems = " , (counter)
for x in items:
	y = 76
	if x == y:
		items.remove(x)

print "Removed 76s from the ArrayList : " , (items)

for item in items:
	if item == True:
		items.remove(item)
print "'True' is at :" , item , " and removed from The ArrayList"
print(items)