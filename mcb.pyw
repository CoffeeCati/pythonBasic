#! /usr/bin/env python3
# mcb.pyw - 存储并载入多重剪贴板
# Usage: py mcb.pyw save <keyword> - 保存当前剪贴板的内容到关键字<keyword>
#        py mcb.pyw <keyword> - 将<keyword>中保存的内容赋值到剪贴板上
#        py mcb.pyw list - 将所有关键字中的内容复制到剪贴板上
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save'
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # TODO: List keywords ans load content

mcbShelf.close()
