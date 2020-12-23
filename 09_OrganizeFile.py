# shutil或称shell工具，里边包含一些函数可以在程序中复制、移动、该改名和删除文件。
import shutil, os

# 复制文件和文件夹
def ofile1():
    # shutil.copy(source, destination) 把source参数的文件复制到destination处，
    # 若destination是一个文件则把复制过去的文件的名字改为destination的文件名即目的文件内容被改变，名字不变
    shutil.copy('./hello.txt', '/Users/liushuo')    # 返回'/Users/liushuo/hello.txt'
    shutil.copy('./hello.txt', '/Users/liushuo/eggs2.txt')  # 返回'/Users/liushuo/eggs2.txt'，此时eggs2.txt内容已经和hello.txt相同

    # copytree()将整个文件夹包括其下的所有自文件，全部复制到目的位置，若目的路径上有的文件不存在，则会新建空文件夹
    shutil.copytree('./', '/Users/liushuo/ofile')   # 返回'/Users/liushuo/ofile'


# 文件和文件夹的移动和改名
def ofile2():
    # shutil.move(source, destination)将source处的文件夹移动到destination，剪切功能
    # 若destination所指文件夹存在，则移动至存在的文件夹下
    # 若destination所指的是一个文件，则source处是文件被移动到destination处后杯改名为destination所指的文件的名，与copy相似
    # 若destination完整路径中有有至少一个不存在的文件夹，则会报错，不会进行移动，不像copy一样会新建
    shutil.move('/Users/liushuo/eggs2.txt', './')   # 返回'./eggs2.txt'

# 永久删除文件和文件夹
def ofile3():
    os.unlike('path')       # 删除path处的文件
    os.rmdir('path')        # 删除path处的文件夹，该文件夹必须为空，里边不能有文件夹或者文件
    shutil.rmtree('path')   # 删除path处的文件夹，包括其中的所有文件夹和文件
    os.listdir()            # 显示当前文件夹下所有文件及文件夹, 括号里可以放入绝对会或相对路径
    for filename in os.listdir():
        if filename.endswith('.txt'):   # 删除当前文件夹下txt文件
            # os.unlink(filename)
            print(filename)     # 最好添加一个print来表示删除了哪个文件

# 使用send2trash模块安全地删除，需要安装'sudo pip3 install send2trash'
# 会把删除的文件放入废纸篓
import send2trash
def ofile4():
    baconFile = open('bacon.txt', 'a')
    baconFile.write('Bacon is not a vegetable.')
    baconFile.close()
    send2trash.send2trash('bacon.txt')

# 遍历目录树, ow.walk()返回一依次3个参数，当前文件夹名称，当前文件夹下的子文件夹组成的list，当前文件下下自文件组成的list
# 会遍历该目录下所有的东西，不仅当前层，一直向下，知道没有任何分支，即该方法很庞大
def ofile5():
    for folderName, subFolder, fileName in os.walk('../'):
        print('The current folder is ' + folderName)

        for subName in subFolder:
            print('SUBFOLDER OF ' + folderName + ': ' + subName)
        for file in fileName:
            print('FILE INSIDE ' + folderName + ': ' + file)

