import re

def strong():
    while True:
        text = input()
        if len(text) < 8:
            print('You have to set the password at least 8 len.')
            continue
        lowRegex = re.compile(r'[a-z]')
        upRegex = re.compile(r'[A-Z]')
        numRegex = re.compile(r'\d+')
        if lowRegex.findall(text) and upRegex.findall(text) and numRegex.findall(text):
            print('Pass!')
            break
        print('At least 1 digit and 1 lowercase and 1 uppercase word')

