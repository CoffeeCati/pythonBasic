'''
    webbrowser: Python自带，打开浏览器获取指定页面
    requests: 从因特网上下载文件和网页
    Beautiful Soup: 解析HTML
    selenium: 启动并控制一个Web浏览器。selenium能填写表单，并模拟鼠标在这个浏览器中点击
'''
import requests

def web1():
    res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
    type(res)       # 返回<class 'requests.models.Response'>
    res.status_code     # 返回200，因为HTTP协议中'OK'的状态码为200
    res.status_code == requests.codes.ok      # 返回True

    len(res.text)       # 返回179380，即179380个字符
    print(res.text[:250])

    res.raise_for_status()      # 下载文件出错时抛出异常, 在requests.get()之后使用，确保下载成功后程序才继续执行

    # 将文件下载到硬盘，需要使用写二进制方法保证Unicode编码，即便是纯文本文件
    playFile = open('RomeoAndJuliet.txt', 'wb')
    for chunk in res.iter_content(100000):      # 使用Response对象的iter_content()做循环
        playFile.write(chunk)
    playFile.close()


# 不要用正则表达式处理HTML，用BeautifulSoup模块解析HTML
import bs4

def web2():
    exampleFile = open('example.html')
    exampleSoup = bs4.BeautifulSoup(exampleFile)
    type(exampleSoup)           # <class 'bs4.BeautifulSoup'>
    elems = exampleSoup.select('#author')
    type(elems)                 # 由id="author"的元素组成的list，每个list元素为一个Tag对象
    elems[0].getText()          # 返回Al Sweigart
    str(elems[0])               # 返回'<span id="author">Al Sweigart</span>'
    elems[0].attrs              # 返回{'id': 'author'}
''' 传给select()方法的选择器                      将匹配...

    soup.select('div')                          所有名为<div>的元素
    soup.select('#author')                      带有id属性为author的元素
    soup.select('.notice')                      所有使用CSS class属性名为notice的元素
    soup.select('div span')                     所有在<div>之间的<span>元素
    soup.select('div > span')                   所有直接在<div>之内的<span>元素，中间没有其他元素
    soup.select('input[name]')                  所有名为<input>，并有一个name属性，其值无所谓
    soup.select('input[type="button"]')         所有名为<input>，并有一个type属性，其值为button的元素
'''

# 通过元素的属性获取数据, 使用Tag对象的get()方法
def web3():
    soup = bs4.BeautifulSoup(open('example.html'))
    spanElem = soup.select('span')[0]
    str(spanElem)           # 返回<spna id="author">Al Sweigart</spna>
    spanElem.get('id')          # 'author'
    spanElem.get('some_nonexistent_addr') == None   # True
    spanElem.attrs          # {'id': 'author'}



