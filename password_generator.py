#! /usr/bin/python3
from sys import argv
from dependencies import getPassword

if len(argv) == 2:
    print (getPassword(argv[1]))
elif len(argv) == 1:
    length = input('Please enter the password length: ')
    print(getPassword(length))
