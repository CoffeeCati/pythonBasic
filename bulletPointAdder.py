#! /usr/bin/env python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line text on the clipboard
'''本项目旨创建一个无序列表，即让每个列表项占据一行，并在前面放置'*'号，并将新的内容复制至剪贴板
    1.从剪贴板粘贴文本
    2.对它做一些处理
    3.将新的文本复制到剪贴板
'''
import pyperclip
text = pyperclip.paste()

# TODO: Seperate lines and add stars TODO在开发时将难点部分标记便于回头再来修改
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]
text = '\n'.join(lines)
print(text)                 # 可以看到输出，该句只是剪贴板可视化
pyperclip.copy(text)

