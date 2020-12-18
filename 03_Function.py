# 使用def定义函数
import random

def hello(name):
    print('Hello ' + name)
hello('Cookie')
hello('sure')

def getAns(ansNumber):
    if ansNumber != 76:
        return 'Wrong! Pls tyr again!'
    else:
        return 'Right!'
while True:
    fortune = random.randint(62, 100)
    print(fortune)
    print(getAns(fortune))         # print(getAns(random.randint(62, 100)))
    if fortune == 76:
        break

# print有可选参数 end和sep，分别表示末尾打印什么(默认为换行符)和多个元素分隔符(默认为空格)
if None == print('xxx'):
    print('print return None')

print('Hello', end='')      # 连接成字符串
print('world')
print('cats', 'dogs', 'mice', sep=',')

# 函数内不能直接修改全局变量，但可以调用, 且全局变量可以声明在调用函数之后，但局部变量要声明在使用之前
def demo():
    print(tmp)
#   tmp -= 9
tmp = 12
demo()

# 可以使用global 定义全局变量
def spam():
    global eggs
    eggs = 'spam'       # global
def bacon():
    eggs = 'bacon'      # local
    print('eggs in bacon: ' + eggs)
eggs = 42               # global
print('before spam:' + str(eggs))
spam()
bacon()
print('After spam and bacon: ' + eggs)

# 使用try和except进行异常处理
def divide(num):
    try:
        return 42 / num
    except ZeroDivisionError:
        print('Error: Invalid argument.')
print(divide(1))
print(divide(2))
print(divide(0))
print(divide(20))
# 一旦程序进入except语句就不会返回try, 如下例不会运行出divide_2(20)
def divide_2(num):
    return 42 / num
def test1():
    try:
        print(divide_2(1))
        print(divide_2(2))
        print(divide_2(0))
        print(divide_2(20))
    except ZeroDivisionError:
        print('Error: Invalid argument.')
test1()