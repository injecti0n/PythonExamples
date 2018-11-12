#/usr/bin/python3
import random
import string
class Cards:
    def __init__(self, type, number):
        self.type = type
        self.number = number

    def __repr__(self):
        return self.type + " of " + self.number



for i in range(1,10):
    s = string.ascii_lowercase
    RandomString = ''.join(random.sample(s,10))
    DOC = Cards(RandomString,str(i))
    print(DOC)

