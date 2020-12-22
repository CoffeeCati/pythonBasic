#! usr/bin/env python3
# phoneEmail.py - 电话号码和Email地址提取程序

import re, pyperclip

'''新知识，一定要注意每一个括号代表的分组，每个括号一定是一个分组，无其他语法意义'''
phoneRegex = re.compile(r'''(           # 整个被匹配的串，是以下部分的拼接
    (\d{3}|\(\d{3}\))?                  # 地区号
    (\s|-|.)?                           # 分隔符
    (\d{3})                             # 前三位
    (\s|-|.)                            # 分隔符
    (\d{4})                             # 后四位
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # 扩展部分，是(ext|x|ext.)和(\d{2,5})的拼接
    )''', re.VERBOSE)               # 共有9个括号，第[0]号为整个串，[6]号为扩展部分整个部分

# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # 用户名
    @                       # @符号
    [a-zA-Z0-9.-]+          # 域名
    (\.[a-zA-Z]{2,4})       # 顶级域名
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    # 因为正则表达式中刚上来就加了括号，这样做使得第[0]号位置为一个被匹配的整串
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])    # 区号+前三位+后四位+分机号
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email addresses found.')

