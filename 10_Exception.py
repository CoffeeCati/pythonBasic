# 使用raise语句抛出异常，raise语句包括
''' 1. raise关键字
    2. 对Exception函数的调用
    3. 传递给Exception函数的字符串，包含有用的出错信息 '''
# 调用Exception该函数的代码知道如何处理异常，而不是Exception本身
def excpt1():
    raise Exception('This is the error message.')       # 如果没有try和except的覆盖而抛出异常的raise语句，程序就会崩溃发出以下内容
''' Traceback (most recent call last):
      File "<input>", line 1, in <module>
    Exception: This is the error message. '''


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' '*(width - 2)) + symbol)
    print(symbol * width)

# 配合try和except一起使用就不会崩溃
for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:            # 把Exception中的内容放入err
        print('An exception happened: ' + str(err))
'''
    ****
    *  *
    *  *
    ****
    00000000000000000000
    0                  0
    0                  0
    0                  0
    00000000000000000000
    An exception happened: Width must be greater than 2.
    An exception happened: Symbol must be a single character string.
'''

# 取得反向跟踪的字符串，如果Python遇到错误就会生成一些错误信息，成为"反向跟踪"
# 其中包括了出错消息，导致该错误的代码行号，以及导致该错误的函数调用的序列，这个序列被称为"调用栈"
# 每次系统崩溃显示的Traceback内容就是反向跟踪，用traceback.format_exc()可以得到它的字符串形式
import  traceback

def spma():
    bacon()
def bacon():
    return
    #raise Exception('This is the error message')

spma()
''' Traceback (most recent call last):
      File "<input>", line 1, in <module>
      File "<input>", line 2, in spma
      File "<input>", line 4, in bacon
    Exception: This is the error message '''

# 断言，由assert语句执行。如果检查失败就会抛出异常，assert语句包含以下部分
''' 1. assert关键字
    2. 条件（即求值为True或False的表达式）
    3. 逗号
    4. 当条件为False时显示的字符串
'''
# 当assert后的东西为False时就立刻崩溃，发出逗号后的内容
def excpt2():
    podBayDoorsStatus = 'open'
    assert podBayDoorsStatus == 'open', 'The pod bay doors need to be "open".'
    podBayDoorsStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
    assert podBayDoorsStatus == 'open', 'The pod bay doors need to be "open".'
'''
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "<input>", line 5, in excpt2
AssertionError: The pod bay doors need to be "open".
'''

# ！！Note: 断言是针对程序员的错误的，抛出异常是针对用户的错误的！！

# 使用logging模块打印日志
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def favtorial(n):
    logging.debug('Start os factorial(%s)' % (n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(favtorial(5))
logging.debug('End of program')
'''
 2020-12-24 19:14:15,456 - DEBUG - Start of program
 2020-12-24 19:14:15,456 - DEBUG - Start os factorial(5)
 2020-12-24 19:14:15,456 - DEBUG - i is 1, total is 1
 2020-12-24 19:14:15,456 - DEBUG - i is 2, total is 2
 2020-12-24 19:14:15,456 - DEBUG - i is 3, total is 6
 2020-12-24 19:14:15,456 - DEBUG - i is 4, total is 24
 2020-12-24 19:14:15,456 - DEBUG - i is 5, total is 120
 2020-12-24 19:14:15,456 - DEBUG - End of factorial(5)
 2020-12-24 19:14:15,456 - DEBUG - End of program
 '''

# 日志级别，从低到高
'''
    DEBUG           logging.debug()             最低
    INFO            logging.info()              
    WARNING         logging.warning()           可能的错误，他不会阻止程序工作，但将来可能会
    ERROR           logging.error()             用于记录错误，它导致程序做错某事
    CRITICAL        logging.critical()          最高，表示致命错误，它导致或将要导致程序完全停止
'''

# logging.disable()可以禁止日志
def excpt3():
    logging.critical('Critical error! Critical error!')
    # CRITICAL:root:Critical error! Critical error
    logging.disable(logging.CRITICAL)           # 禁用所有等级的日志
    logging.critical('Critical error! Critical error!')
    logging.error('Error error! Error error!')

# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# 可以将level参数设置为logging.Error，这样日志中只会显示ERROR和CRITICAL消息

# 将日志记录到文件
def except4():
    logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='\
    %(asctime)s - %(levelname)s - %(message)s')



