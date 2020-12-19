# print中添加r可以让转义字符失效，但不会因未转义导致可能提前停止输出的问题，如转义\', \''失败，并不会让后续字符串无效
def tset1():
    print(r'hello world\n i\'m lihua')


# '''或"""即连续的3个单引号或双引号，会使得之间的所有字符都被输出，包括空格,转义字符,单双引号,函数内部的缩进
# 这里所谓的"函数内部缩进"实质也不是函数内部的缩进，因为仍属于一句代码print()内部
def test2():
    print('''Dear Alice,
    
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
    
Sincerely
Bob''')


# 连续的三个'或"还可以用来进行多行注释

s1 = 'Hello world'


def cut():
    # 对应下标，用于切片
    # ' H e l l o   w o r l d '
    #   0 1 2 3 4 5 6 7 8 9 10 11
    print(s1[6:])  # 'world'
    print(s1[:10])  # 'Hello worl'
    buff = s1[:5]  # buff = 'Hello'


# 使用in或者not in判断字串是否在主串中
def judge():
    global s1
    if 'Hello ' in s1:
        print('"Hello " in here')
    if 'word' not in s1:
        print('"word" not in here')


# string方法upper(), lower(), isupper(), islower()
def isup_low():
    global s1
    s1.upper()  # 不改变s1，但是返回字母大写的字符串，如果想改变s1应使用s1 = s1.upper()
    s1.lower()  # 同上，都是只对字母操作，其他字符不受影响
    s1.isupper()  # 返回bool类型，只有当s1至少有一个字母且全部字母全大写才返回True
    s1.islower()  # 同上
    ' '.islower()  # 空格等其他字符如符号，数字等既不是小写也不是大写，当只有这些符号而没有字母时返回False
    # 若字符串中有字母和这些符号则以字母为准


# isX字符串方法，均返回bool类型
def isX():
    'hello'.isalpha()  # 只有字母
    'hello123'.isalnum()  # 只有数字或字母或二者结合，与c/c++同
    '123214'.isdecimal()  # 只有数字
    ' \t \n'.isspace()  # 只有空格制表符和换行符
    'This Is Tile Case 123'.istitle()  # 每个单词的首字母大写且后续字母小写
    'This Is not Title'.istitle()
    'This Is NOT Title CAse Either'.istitle()


# startswith()和endswith()返回bool，分别判断是否以某个前缀开始或以某个后缀结束，这里"前后缀"可以包含整个串，与kmp的next不同
def starts_ends():
    'starts with starts'.startswith('st')
    'ends with ends'.endswith('nds')


# join()和spilt()用于连接和拆分
def join_spilt():
    # join()的调用对象为list类型，插在每个字符串的中间
    print(', '.join(['cats', 'dogs', 'bats']))
    print(' '.join(['My', 'name', 'is', 'Simon']))
    # split()将分隔符调入参数，默认为' '，返回list类型
    print('My name is Simon'.split())
    print('MyABCnameABCisABCSimon'.split('ABC'))


# rjust(), ljust(), center()方法对齐文本有两个参数，第二个为可选参数
def just():
    print('Hello'.rjust(10))  # 向右调整为长度为10，因为'Hello'长度为5，所以即在左边添加5个' '
    print('hello'.rjust(10, '*'))  # 在左边添加5个'*'
    print('hello'.ljust(20, '-'))  # 在右边添加15个'-'
    print('hello'.center(20, '='))  # 填充'='使得长度为20并让'hello'居中
    # 以上三个方法，参数相同，只是调整方法不同，偏移量均以<第一个打印字符位置>为基准，不是第每次都在屏幕左侧


# 利用just制作表格，第一列长度为leftWidth，第二列长度为rightWidth
def printPicnic(itemDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for i, j in itemDict.items():
        print(i.ljust(leftWidth, '.') + str(j).rjust(rightWidth))


picnicItems = {'sanwichs': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 4)
printPicnic(picnicItems, 20, 6)


# strip(), rstrip(), lstrip()删除空白字符，有一个可选参数
def Strip():
    spma = '   Hello world   '
    print(spma.rstrip())  # 删除右侧的空白符
    print(spma.lstrip())  # 删除左侧的空白符
    print(spma.strip())  # 删除两侧的空白符
    spma2 = 'SpmaSpmaBaconSpmaEggsSpmapSma'
    print(spma2.strip('ampS'))  # 参数内部顺序不重要，自我猜测python删除方式是按长度比对，若字母个数和字母类型相同则删除


# 使用pyperclip模块拷贝粘贴字符串
import pyperclip

pyperclip.copy('Hello world')
pyperclip.paste()
