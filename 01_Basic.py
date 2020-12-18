print('hello world')
print('What is your name')
myName = input()
print('it is goo meet you' + myName)
print('The length of your name is:')
print(len(myName))
print('What is you age')
myAge = input()             # input()求值为字符串
print('you will be ' + str(int(myAge) + 1) + ' in a year')  # myName为字符串，必须使用int转化成整形
