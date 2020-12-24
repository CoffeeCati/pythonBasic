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

# 用zipfile模块压缩文件
import zipfile, os

# 查看压缩文件的内容
def ofile6():
    os.chdir('/Users/liushuo')
    exampleZip = zipfile.ZipFile('example.zip')     # 返回ZipFile对象
    exampleZip.namelist()       # 返回压缩文件内所有的文件夹文件及文件夹对应的子文件
    spmaInfo = exampleZip.getinfo()     # ZipFile的getinfo()方法获取文件有用的信息，大小等
    spmaInfo.file_size          # 返回文件原本大小
    spmaInfo.compress_size      # 返回压缩后大小
    print('Compressed file is %sx smaller.' % (round(spmaInfo.file_size / spmaInfo.compress_size, 2)))
    # 输出压缩效率
    exampleZip.close()

# 文件中解压缩
def ofile7():
    os.chdir('/Users/liushuo')
    exampleZip = zipfile.ZipFile('example.zip')
    exampleZip.extractall()     # 全部解压到当前工作目录，或输入参数使其解压到指定目录
    exampleZip.extract('haha.txt', '/Users')        # 解压单个文件至目标目录下
    # 以上两种extract如果传入目标目录，则路径中不存在的文件夹会被新建
    exampleZip.close()

# 创建和添加到ZIP文件
def ofile8():
    newZip = zipfile.ZipFile('new.zip', 'w')        # 必须以写模式打开，像open()一样输入'w'，'a'
    newZip.write('haha.txt', compress_type=zipfile.ZIP_DEFLATED)    # 指定deflate压缩算法，适用于所有数据类型
    newZip.close()

