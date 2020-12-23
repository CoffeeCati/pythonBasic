#! /usr/bin/env python3
# mcb.pyw - 存储并载入多重剪贴板
# Usage: py mcb.pyw save <keyword> - 保存当前剪贴板的内容到关键字<keyword>
#        py mcb.pyw <keyword> - 将<keyword>中保存的内容赋值到剪贴板上
#        py mcb.pyw list - 将所有关键字中的内容复制到剪贴板上
''' 新知识，.pyw后缀的python程序运行时不会打开终端
    shelve理解为永久的hash比较好
    sys.argv的大小等于用户输入参数的个数-1，因为argv[0]始终为程序文件名'''
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')       # 永久存储，可以认为shelve是一个永久存在的字典，也可理解为Hash

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':     # argv第一个参数[0]是文件名，接着是后续跟着的参数
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:                # 长度为2表示用户只输入了一个参数
    # List keywords ans load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(str(mcbShelf[sys.argv[1]]))

mcbShelf.close()
