# 不使用正则表达式匹配电话号码415-555-4242
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True
print('415-555-4242 is a phone number:\n' + str(isPhoneNumber('415-555-4242')))
print('Moshi moshi is a phone number:\n' + str(isPhoneNumber('Moshi moshi')))


# 装入新的程序，用于处理长文本中的电话，代替上边两个print
def test1():
    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    for i in range(len(message)):
        chunk = message[i:i + 12]
        if isPhoneNumber(chunk):
            print('Phone number found: ' + chunk)
    print('Done')
test1()

# 正则表达式，简称regex \d是一个正则表达式，表示为一位数字字符0～9，故可以使用\d\d\d-\d\d\d-\d\d\d\d来代替上述isPhoneNumber()
# 要导入模块re re.compile()传入一个字符串值，表示正则表达式，他将返回一个Regex对象
import re
def re1():
    phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # 等价于re.compile('\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d')，明显使用r前缀更好
    mo = phoneNumberRegex.search('My number is 415-555-4242')  # 使用serch()将返回一个Match的对象，如果没有则返回None
    print('Phone number found: ' + mo.group())  # Match对象有group()方法，返回被查找字符串中匹配的文本


# 用正则表达式匹配更多模式，使用括号()进行分组，然后使用参数来返回不同的串
def re2():
    phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')  # 将区号分离出来，即将前三位分离出来
    mo = phoneNumberRegex.search('My number is 415-555-4242')
    mo.group(1)  # 返回分组1匹配到的结果，'415'
    mo.group(2)  # 返回分组2匹配到的结果，'555-4242'
    mo.group(0)  # 返回所有拼接起来的结果，'415-555-4242'
    mo.group()   # 与group(0)一样
    mo.groups()  # 返回所有匹配的元素组成的tuple
    # compile中特殊用法:
    # 指定分组名(?P<name>)       引用指定分组(?P=name)
    # \2 引用第二组


# 由于括号在正则匹配中有其他意义，故想要对括号匹配时即便用r前缀，也要使用转义\(***\)
def re3():
    phoneNumberRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
    mo = phoneNumberRegex.search('My number is (415) 555-4242')
    mo.group(1)  # '(415)'
    mo.group(2)  # '555-4242'


# 用"管道"匹配多个表达式中的一个 符号|，当文本中具有多个匹配的表达式时只返回文本中的第一个
# 使用findall() 可以返回所有匹配成功的模式串，并将它们组成一个list
def re4():
    heroRegex = re.compile(r'Batman|Tina Fey')
    mo1 = heroRegex.search('Batman and Tina Fey')
    mo1.group()  # 返回'Batman'

    mo2 = heroRegex.search('Tina Fey and Batman')
    mo2.group()  # 返回'Tina Fey'

    mo3 = heroRegex.findall('Tina Fey and Batman')
    mo3  # 返回['Tina Fey', 'Batman']


# 还可以使用管道指定前缀，通过括号来实现
def re5():
    batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
    mo = batRegex.search('Batmobile lost a wheel')
    mo.group()      # 返回'Batmobile'
    mo.group(1)     # 返回'mobile'


# 用问号实现可选匹配(匹配0次或1次)。括号内的'hello world'为可选分组，出现1次或0次都可以被匹配
# 理解：?前边的分组出现1次或不出现都算匹配成功
def re6():
    batRegex = re.compile(r'Bat(hello world)?man')
    mo1 = batRegex.search('The Adventures of Batman')
    mo1.group()  # 返回'Batman'

    mo2 = batRegex.search('The Adventures of Bathello worldman')
    mo2.group()  # 返回'Bathello worldman'


# 可以实现对前边匹配电话号码的例子，对区号进行可选匹配
def test3():
    phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
    mo1 = phoneRegex.search('My number is 414-555-9999')
    mo1.group()  # 返回'414-555-9999'

    mo2 = phoneRegex.search('My number is 555-9999')
    mo2.group()  # 返回'555-9999'


# 用星号匹配0次或多次，问号只能匹配0或1次，注意区分 *比?更强大
# 理解：*前的分组，出现1次或多次或不出现都算匹配成功
def re7():
    batRegex = re.compile(r'Bat(wo)*man')
    mo1 = batRegex.search('hello Batman')
    mo1.group()  # 返回'Batman'

    mo2 = batRegex.search('hello Batwoman')
    mo2.group()  # 返回'Batwoman'

    mo3 = batRegex.search('hello Batwowowowowowoman')
    mo3.group()  # 返回'Batwowowowowowoman'


# 用加号匹配1次或多次
# 理解：+前的分组至少出现一次算成功匹配
def re8():
    batRegex = re.compile(r'Bat(wo)+man')
    mo1 = batRegex.search('The Adventures of Batwoman')
    mo1.group()  # 返回'Batwoman'

    mo2 = batRegex.search('The Adventures of Batwowowoman')
    mo2.group()  # 返回'Batwowowoman'

    mo3 = batRegex.search('The Adventures of Batman')
    mo3 == None  # 返回Ture

''' *是?和+的并集 '''


# 使用花括号匹配特定次数
# 理解：{a, b}前的分组至少出现a次至多出现b次算匹配成功。a不填则默认为0，b不填则默认为inf，若不加逗号就按输入的固定次数
def re9():
    haRegex = re.compile(r'(Ha){3}')
    mo1 = haRegex.search('HaHaHa')
    mo1.group()  # 返回'HaHaHa'

    mo2 = haRegex.search('HaHa')
    mo2 == None  # 返回True


# {}使用贪心匹配，指定上下界a,b后返回第一个匹配到的且最长的一个
# 如(ha){2,5} 'hahaha and hahahahaha'会返回'hahaha'即使'haha'满足也不会返回，因为贪心
# {}非贪心版本使用?来实现，这里与可选分组不冲突，因为这里是和{}一起使用的，0次或1次是单独使用的
# 同样*?和+?也属于非贪心
def re10():
    nongreedyHaRegex = re.compile(r'(ha){2,5}?')
    mo = nongreedyHaRegex.search('hahaha and hahahaha')
    mo.group()      # 返回'haha'


# findall()方法返回list类型，当分组匹配时则返回元素为tuple的list
def re11():
    phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
    mo = phoneNumberRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
    print(mo)       # [('415', '555', '9999'), ('212', '555', '0000')]


'''常用缩写字符分类
\d      0~9的任何数字
\D      除0～9数字以外的任何字符
\w      任何字母、数字或下划线（可以认为是匹配"单词"的字符）
\W      除字母、数字和下划线以外的任何字符
\s      空格、制表符或换行符（可以认为是匹配"空白"字符）
\S      除空格、制表符和换行符以外的任何字符
字符分类[0-5]可以只匹配数字0～5
'''
def re12():
    xmaxRegex = re.compile(r'\d+\s\w+')
    xmaxRegex.findall('12 drummers, 11 pipers, 10 lords')    # 返回['12 drummers', '11 pipers', '10 lords']


# 建立自己的字符分类，使用[]限定想要匹配的内容
def re13():
    vowelRegex = re.compile(r'[aeiouAEIOU]')        # Note: 在[]内，普通的正则表达式符号不会被解释，如*, ?, (), +都只是想要匹配的符号
    vowelRegex.findall('Hello world all people')    # 返回['e', 'o', 'o', 'a', 'e', 'o', 'e']
    Regex = re.compile(r'[0-5ok]')
    Regex.findall('7895o0jk2')      # 返回['5', 'o', '0', 'k', '2']
# 在[]内的开头加上^表示非，即除后续的字符以外的任何字符都被匹配
def re14():
    consonantRegex = re.compile(r'[^aeiouAEIOU]')
    consonantRegex.findall('hello world')           # 返回['h', 'l', 'l', ' ', 'w', 'r', 'l', 'd']


# 在正则表达式，而不是字符分类开头添加^表示必须以后续的字符串为开头，注意是整个字符串必须这样才可以，而不是部分字串
def re15():
    beginRegex = re.compile(r'^Hello')              # 匹配且仅匹配'Hello'这5个字符
    mo1 = beginRegex.search('Hello world')          # mo1成功匹配'Hello'
    mo2 = beginRegex.search('He said Hello')        # mo2 == None

    endsRegex = re.compile(r'\d$')                  # 匹配且仅匹配最后一个字符为0～9的字符串，和\d+$不同
    endsRegex.search('Your age is 42')              # 成功匹配最后一个'2'

    wholeRegex = re.compile(r'^\d+$')       # 匹配从头到尾均是数字的字符串
    wholeRegex.search('0123456789')         # 成功匹配'0123456789'
    wholeRegex.search('01234xy z56789')      # 匹配失败，返回None


# 正则表达式中.字符成为通配符，匹配除换行之外的所有字符(仅匹配1个)，空格也可以被匹配
def re16():
    atRegex = re.compile(r'.at')
    atRegex.findall('The cat in the hat sat on the flat mat')   # 返回['cat', 'hat', 'sat', 'lat', 'mat']
    atRegex.findall('1at flat cat atat')        # 返回['1at', 'lat', 'cat', ' at']
    # flat 只匹配了 lat 很明显只匹配1个大小


# 用点-星匹配所有非换行字符，很好理解.匹配非空字符，*代表出现或不出现，加起来就是匹配空或不空的全部字符
# 点-星使用贪心匹配
def re17():
    nameRege = re.compile(r'First Name: (.*) Last Name:(.*)')       # 第二个(.*)与前边的:之间无空格，但是仍然可以匹配成功
    mo = nameRege.search('First Name: A1 Last Name: Sweigart')
    mo.group()      # 返回'First Name: Al Last Name: Sweigart'
    mo.group(1)     # 'A1'
# 非贪心版本要在后边加?，和特定次数{}类似
def re18():
    nongreedyRegex = re.compile(r'<.*?>')
    greedyRegex = re.compile(r'<.*>')
    s = '<To serve man> for dinner.>'
    mo1 = nongreedyRegex.search(s)
    mo2 = greedyRegex.search(s)
    print(mo1.group())          # '<To serve man>'
    print(mo2.group())          # '<To serve man> for dinner.>'


# 用句点字符匹配换行，通过传入re.DOTALL作为compile的第二个参数可以让.匹配所有字符
def re19():
    s = 'Serve the trust.\nProtect the innocent.\nUphold the law.'
    noNewlineRegex = re.compile('.*')
    noNewlineRegex.search(s).group()    # 'Serve the trust.'

    newlineRegex = re.compile('.*', re.DOTALL)
    newlineRegex.search(s).group()      # 'Serve the trust.\nProtect the innocent.\nUphold the law.'


# 不区分大小写的匹配，将re.I调用至第二个参数
def re20():
    robocop = re.compile(r'robocop', re.I)
    robocop.search('RoBoCop is part man, part machine, all cop.').group()   # 返回'RoBoCop'


# re模块用sub()方法替换字符 第一个参数为用于替换匹配到的字符串，第二个参数是被匹配的主串
# !!Note: 会替换掉所有被匹配到的字串，这点是理解传入方法时的关键
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
def re21():
    namesRegex = re.compile(r'Agent \w+')       # 替换所有匹配到的字串
    namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
    # 返回'CENSORED gave the secret documents to CENSORED'
# sub()的第一个参数可以调用匹配到的串的参数
    # 当sub的第一个参数为一个方法时则该方法必须只能接收一个参数，且sub第二参数应放入一个字符串用于替换， func提供替换的方式
    # 相当于是先匹配放入group中然后再将匹配到的东西放入func中
    p = re.compile(r'(\w+) (\w+)')
    s = 'i say, hello world'
    p.sub(func, s)   # 返回'I Say, Hello World'
    ''' 若compile中使用了分组，sub中还可以使用\id或\g<id>来引用第id组，或\g<name>引用名为name的组来替换 '''
    p.sub(r'\2 \1', s)          # 'say i, world, hello'
    p = re.compile(r'(?P<word1>\w+) (?P<word2>\w+)')
    p.sub(r'\word2 \word1', s)  # 与p.sub(r'\2 \1')结果相同


def re22():
    agentNamesRegex = re.compile(r'Agent (\w)\w*')
    agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve')   # \1会自动换成group第一个参数的内容，即(\w)分组
    # 返回'A**** told C**** that E****'


# 当正则表达式过于复杂时会让程序员的理解变得困难，可以引入re.VERBOSE作为compile()第二哥参数，让compile()忽视表达式中的空格和换行
def re23():
    phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?              # area code
        (\s|-|\.)?                      # separator
        \d{3}                           # first 3 digits
        (\s|-|\.)                       # seperator
        \d{4}                           # last 4 digits
        (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
    )''', re.VERBOSE)
    mo = phoneRegex.search('My number is (415) 555-4242')
    mo.group()          # '(415) 555-4242'


# 组合使用re.I, re.DOTALL和re.VERBOSE, 由于compile只支持2个参数，故使用｜将其组合
someRegexValues = re.compile('foo', re.I | re.DOTALL | re.VERBOSE)

