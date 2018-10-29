#!/usr/bin/python3

print "Injecti0n Login"


loop = True
while (loop == True):
    username = raw_input("Please enter your username: ")
    if (username=='root'):
    	password = raw_input("Please enter your password: ")
        if (password == '1234'):
            print "Logged in successfully as " + username
            loop = False
        else:
            print "Password incorrect!"
    else:
        print "Username incorrect!"