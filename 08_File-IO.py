# 写在前面
# windows系统在路径表示用\分开，代码中的路径用\\分开，因为每个\又需要一个\来转义，根文件夹为C:\
# 在OS X和Linux中用/分开，代码中也用/，且根文件夹表示为/

# 导入OS模块，保证程序可以在所有操作系统中使用对应正确的路径
import os

os.path.join('usr', 'bin', 'spma')  # OS X上返回'usr/bin/spma'

def f1():
    myFiles = ['accounts.txt', 'detail.csv', 'invite.docx']
    for filename in myFiles:
        print(os.path.join('/usr/bin', filename))
# f1()

# 当前工作目录
def f2():
    os.getcwd()         # 获取当前工作目录
    os.chdir('/usr')    # 改变工作目录

# 绝对路径和相对路径 .是当前路径的缩写而..是父文件夹，
# 打开当前工作目录下的文件xxx.py时，为./xxx.py。打开兄弟文件spma.txt时，为../spma.txt

# os.makedirs()创建新的文件夹，路径任意，实际操作来只能创建文件夹，不能指定后缀来改变类型
    os.makedirs('/usr/delicious/walnut/waffles')    # 创建delicious文件夹-->创建walnut文件夹-->创建waffles文件夹

# 处理绝对路径和相对路径
def f4():
    os.path.abspath('.')        # 相对路径作为参数，返回绝对路径
    os.path.isabs('/usr')       # 判断参数的路径是否为绝对路径，返回bool
    os.path.relpath(path, start)    # 返回从start到path的相对路径，如果没有提供start就以当前工作目录作为开始
    os.path.relpath('/Users')   # 区分大小写

# 分割路径
def f5():
    path = '/usr/bin/env'
    os.path.basename(path)      # 返回最后一层，基本名称，'env'
    os.path.dirname(path)       # 返回前边目录名称，'/usr/bin'
    os.path.split(path)         # 返回二者组成的tuple ('/usr/bin', 'env')
    (os.path.dirname(path), os.path.basename(path))     # 和调用os.path.split(path)返回值相同
    path.split(os.path.sep)     # 可以根据操作系统的不同把路径中每一个文件夹分割出来，返回组成的list

# 查看文件大小和文件内容
def f6():
    path = '/usr/bin/'
    os.path.getsize(path)       # 返回path所在文件夹或文件的字节数Byte
    os.listdir(path)            # 返回文件夹下所有文件构成的list，只能在path表示文件夹时起作用

# 防止犯错，检查路径有效性
def f7():
    os.path.exists('/usr/bin')  # 返回bool，如果文件/文件夹存在则返回True
    os.path.isfile('/usr/bin/env')  # 返回bool，如果该路径存在且指向文件，则返回True
    os.path.isdir('/usr')       # 返回bool，如果该路径存在且指向文件夹，则返回True

# 读写文件，特指处理纯文本文件而非二进制文件
''' 读写文件具有3个步骤
    1.调用open()，返回一个File对象
    2.调用File对象的read()和write()方法
    3.调用File对象的close()方法，关闭该文件
    '''
# 操作发现读文件时，每次open只能读一次，之后只返回''
# 如果open()的文件不存在，则写模式'r'和添加模式'a'都会创建一个新的文件，并且当'w'和'a'模式时，只有close后才能看到文件的变化
def f8():
    helloFile = open('hello.txt')      # open()接受绝对路径也接受相对路径，接受第二参数，传'r'或不传表示只能读
    helloFile.read()            # 返回整个文件的内容作为一整个大的字符串
    helloFile.readlines()       # 每一行作为一个字符串，返回list，且除最后一行外每一行以'\n'结尾
    baconFile = open('hello.txt', 'w')  # 向第二个参数传递'w'表示可以写，但是会全部覆盖原有文本
    # 可以理解为使用该语句后文件被清空并进入让baconFile编辑阶段，即多次调用baconFile.write()会累加，而不会覆盖掉上次write()添加的内容
    baconFile.write('Hello world!\n')    # 写入文件并返回写入了多少个字符

    baconFile = open('./hello.txt', 'a')    # 调用write()时添加在原文本后边
    baconFile.write('This is the second line.')

# 用shelve模块保存变量，将Python程序中的变量保存到二进制的shelf文件中，这样程序就可以从硬盘中恢复变量的数据
import shelve

def f9():
    shelfFile = shelve.open('mydata')   # shelve模式不必选择读或写模式，因为打开以后两者皆可
    cats = ['Zophie', 'Pooka', 'Simon']
    shelfFile['cats'] = cats            # 像字典一样进行修改，可以永久保存在硬盘里，保存变量cats
    shelfFile.close()
# 下次使用时可用list(shelfFile.keys())查看键值

# 用文件保存变量
def f10():
    import pprint
    cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
    pprint.pformat(cats)        # 排序，返回"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
    fileObj = open('myCats.py', 'w')
    fileObj.write('cats = ' + pprint.pformat(cats) + '\n')  # 保存变量cats
    import myCats           # 使用import不仅可以引入模块还可以引入其他文件
    myCats.cats[0]['name']  # 返回'Zophie'
    # 可用myCats.cats返回cats变量的内容
