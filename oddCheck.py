#!/usr/bin/python3
import random
'''
  _       _           _   _  ___        
 (_)     (_)         | | (_)/ _ \       
  _ _ __  _  ___  ___| |_ _| | | |_ __  
 | | '_ \| |/ _ \/ __| __| | | | | '_ \ 
 | | | | | |  __/ (__| |_| | |_| | | | |
 |_|_| |_| |\___|\___|\__|_|\___/|_| |_|
        _/ |                            
       |__/                             
       '''
       # Odd Check from ArrayList
def OddChecker(number):
		if (number % 2 ==0):
			print "odd! : ", number

	 

myArray = []
for x in range(1,101):
	myArray.append(x)


print myArray
for numbers in myArray:
	OddChecker(numbers)	

	




