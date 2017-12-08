from random import randint
def isInt(x):
    for i in str(x):
        if i not in '1234567890':
            return False
    return True



def getPassword(pass_len):
    if isInt(pass_len):
        strings = 'abcdefghijklmnopqrstuvwxyz'
        upperStrings = strings.upper()
        numbers = '123456789'
        specialCharacters = '~`@#$%^&*()-=[]\\;\',./{}:"<>?'
        types = [strings, upperStrings, numbers, specialCharacters]
        password = ''
        for i in range(0, int(pass_len)):
            parentType = types[randint(0, len(types) - 1)]
            randomCharacter = parentType[randint(0, len(parentType) - 1)]
            password += randomCharacter
        return password
    else:
        return("We need an integer as the length of the password!")
