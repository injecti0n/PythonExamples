#!/usr/bin/python3
import string



def encrypt(myString, shift):
    cipher = ''
    for char in myString:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

    return cipher

def decrypt(shift, myString):
    key = string.ascii_lowercase
    result = ''

    for l in myString:
        try:
            i = (key.index(l) - shift) % 26
            result += key[i]
        except ValueError:
            result += l

        print(result)


def mainMenu():

    userChoice = input("Encrypt[1]\n" + "Decrypt[2]\n" + "What is your choice? : ")
    if userChoice == "1":
        yourMessage = input("Your message = ")
        shift = int(input("enter shift number: "))
        print("original string: ", yourMessage)
        print("after encryption: ", encrypt(yourMessage, shift))
    else:
        myString = input("Encrypted text = ")
        shift = int(input("enter shift number: "))
        decrypt(shift,myString)


while(True):
    mainMenu()

