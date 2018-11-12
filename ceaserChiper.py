#!/usr/bin/python3
import string

def load_file(filename):
    with open(filename, 'r') as f:
        contents = f.read()
    return contents

def save_file(filename, data):
    with open(filename, 'a') as f:
        f.write(data)

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
        filename = '/home/intec/Desktop/pythonTuto/' + myString + '.txt'
        save_file(filename,result)


def mainMenu():


    userChoice = input("Encrypt[1]\n" + "Decrypt[2]\n" + "What is your choice? : ")
    if userChoice == "1":
        StringOrFile = input("From String or File? [1] [2] = ")
        if StringOrFile == "1":
            yourMessage = input("Your message = ")
            shift = int(input("enter shift number: "))
            print("original string: ", yourMessage)
            print("after encryption: ", encrypt(yourMessage, shift))
        else:
            shift = int(input("enter shift number: "))
            myString = input("Enter filename: ")
            filename = load_file('/home/intec/Desktop/pythonTuto/' + myString + '.txt')
            print(filename)

            print("after encryption: ", encrypt(filename, shift))
            AskForSave = input("Do you want to save it? type [yes] or [no]")
            if AskForSave == 'yes':
                encString = encrypt(filename, shift)
                save_file(filename, encString)
            else:
                print("null")
                
            
    else:
        myString = input("Encrypted text = ")
        shift = int(input("enter shift number: "))
        decrypt(shift,myString)


while(True):
    mainMenu()


