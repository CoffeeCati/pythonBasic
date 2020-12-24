#! /usr/bin/env python3
# backupToZip.py - 将一个文件夹里的内容全部备份到一个ZIP文件，ZIP文件名为xxx_1.zip每次新建后边的数字会增加
import os, zipfile

def backupToZip(folder):
    folder = os.path.abspath(folder)        # 保证路径是绝对路径

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'     # 确定ZIP的文件名序号
        if not os.path.exists(zipFilename):
            break
        number += 1

    # Create the ZIP file
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Work the entire folder tree and compress the files in each folder.
    for folderName, subfolderName, fileNames in os.walk(folder):
        print('Adding files in %s...' % (folderName))
        backupZip.write(folderName)          # 把当前目录放入ZIP文件中
    for filename in fileNames:
        newBase = os.path.basename(folder) + '_'
        if filename.startswith(newBase) and filename.endswith('.zip'):      # 把已经是压缩文件的文件排除掉
            continue
        backupZip.write(os.path.join(folderName, filename))
    backupZip.close()

backupToZip('./')

