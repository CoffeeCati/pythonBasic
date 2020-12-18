# List比数组更强大，可以包括多种元素类型，可以使用切片[0:4]指取出0-3号共4个元素，且提供二维表示
# [-1]表示最后一个元素, [0:-1]取除了最后一个元素的其他元素 [:]取全部元素
spam = ['1', '2', '3']
spam = spam + ['a', 'b', 'c', 789]
print(spam)

del spam[2]  # 删除指定位置，使得后续位置元素前移spma[2] = '3'
print(spam[2])   # spma[2] = 'a'

# 列表的添加使用spma = spma + [const]  其中const为非列表变量
catName = []
while True:
    print('Enter the name of  cat ' + str(len(catName)+1) + ' (Or Enter nothing to stop.):')
    name = input()
    if name == '':
        break
    else:
        catName += [name]
print('The cat name are:')
for name in catName:
    print(' ' + name)

# list-----for
for i in [0, 2, 5, 8, 'bye']:
    print(i)

someList = ['pens', 27, 29.54, 'see you']
for i in range(len(someList)):
    print(someList[i])

# 多重赋值，保证list大小和被赋值变量个数相同才可以
cat = ['fat', 'black', 'loud']
size, color, disposition = cat
print(size, color, disposition, sep=',')

# list数据类型的方法(类函数)
demo = [123, 'hello', 'hi', 'howdy', 'hi', 'heyas']
demo.index('hello')     # index()查找列表中的元素的下标，若不存在则返回异常ValueError，存在多个则返回第一次出现的位置
demo.append('moose')    # append()在后边添加元素，相当于demo += ['moose']
demo.insert(1, 'chicken') # insert()插入指定下标，当前元素及后续元素后移
demo.remove(123)        # remove()删除指定内容，与del demo[0]结果相同是删除指定下标处的值，Note！！<----只删除第一次出现的位置
demo.sort()             # sort()可以有参数key，按照某种方式排序，若不加参数，则按升序，Note！！<--排序的list不能同时包含数字和字符
                        # 且对字符串排序是按照ASCII字符顺序，不是按实际字典序
demo.sort(key=str.lower)  # 按字典序升序

print('Hell' + \
      'o World')        # 用\续行要保证\符号所在行是最后一个字符，注释也不能写在对应的那一行，也不能有后续的空格
                        # 但就实际操作发现好像加不加\效果是一样的
# 字符串也具有一些list的特性，如用in/not in判断某字符串是否在主串中，或者切片截取，随机访问
name = 'Cookie'
for i in name:
    print('*****' + i + '*****')
'Cook' in name == True

# 对字符串修改时与list不同，不能直接使用下标修改
name = 'Catch a cat'
name = name[:6] + 'the' + name[7:]  #保留0->5 and 7->(-1)的字符串
print(name)                 # Catch the cat

# 元组tuple与list基本一样，只是不能进行修改，不可变
eggs = ('hello', 42, 0.5)
type(('string'))
type(('tuple',))       # 元组中只有一个元素时要加逗号，否则将算作一个普通的类型

# tuple list str可以强制转换，即想修改tuple可以转化成list再换回去
tuple(['cat', 'dog', 5])
list(('cat', 'dog', 5))
list('hello')

# list赋予别的变量值后，在新的变量上修改，原变量也会被修改------引用
source = [0, 1, 2, 3, 4, 5]
change = source
change[0] = 'hello'
print(change)
print(source)
# 放到函数的参数中也一样直接被修改
def func(tmp):
    tmp.append('hello')
func(source)
print(source)

# copy模块，包含copy()以及deepcopy()
import copy
spam2 = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam2)       # 使用copy使得spam2和cheese指向两个不同的列表
cheese[2] = 43
print(spam2)
print(cheese)
# 当list中的元素有list类型时，使用deepcopy使其具有独立性


