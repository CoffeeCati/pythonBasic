#! /usr/bin/env python3
# pw.py - An insecure password locker program
# 口令保管箱项目（不安全）
# description: 使用用口令管理器软件，利用一个主控口令，解锁口令管理器。然后将某个账户口令拷贝到粘贴板，再将它粘贴到网站的口令输入框
''' <新知识>: OS X使用Terminal运行py程序，程序首行如本文件第一行所示让操作系统找到python编辑器，cd ~表示回到主文件夹，
    pwd可以显示当前工作目录，cd到本文件所在目录，使用命令chmod +x pw.py可以使之成为可执行文件，输入./pw.py可以运行该脚本 '''
PASSWORDS = {'email': 'F7minBDDuvMJuxESSKHFhTxFtjVB86',
             'blog': 'VmA138jjjGYGWowdqdhi9',
             'luggage': '12345'}
# 命令行参数将存储在sys.argv中，sys.argv是一个列表，其中第一个元素总是字符串，包含文件名('pw.py')，第二项应该是第一个命令行参数
# 对于本程序，这个参数就是账户名称，由用户提供。因为命令行参数是必须的，如果用户忘记添加该参数应进行提醒
import sys, pyperclip
if len(sys.argv) < 2:
    print('Uage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # 第一个命令行参数是账户名称

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
# 运行程序时输入./pw.py <aacount name>即可
