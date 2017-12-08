#! /usr/bin/python3
from sys import argv
from dependencies import getPassword, isInt

if len(argv) == 2 and isInt(argv[1]):
    print (getPassword(argv[1]))
else:
    length = input('Please enter the password length: ')
    print(getPassword(length))
