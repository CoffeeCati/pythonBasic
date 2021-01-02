#! /usr/bin/env python3
# 11_mapIt.py - 将一条街道的地址拷贝到剪贴板，并在网页上打开它的地图
'''
    1. 从sys.argv读取命令行参数
    2. 读取剪贴板内容
    3. 调用webbrowser.open()函数打开外部浏览器
    https://www.amap.com/place/B02270JPFF - AHU鸣磬广场
'''
import webbrowser, sys, pyperclip

# 若sys.argv长度大于1则说明用户输入了参数，砍掉第一个元素即文件名11.mapIt.py
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()     # 用户没有输出参数则从剪贴板读取内容

webbrowser.open('https://www.amap.com/place/' + address)


