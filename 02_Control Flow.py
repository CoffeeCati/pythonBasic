import sys, math, os, random

for i in range(10, -2, -1):     # 起始，>终止(=终止+1)，步长
    print(random.randint(1, 100))      # 随机数

while True:
    s = input()
    if s == 'exit':
        sys.exit()              # 退出程序
    print('You type "' + s + '".')
