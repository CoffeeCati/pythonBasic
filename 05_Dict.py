# 字典应该就是Hash, key值任意类型，value值任意类型，使用{}
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
spma = {12345: 'left', 42: 'right'}

# 字典不会进行排序也就不能像list一样使用切片进行访问，但是dict顺序不同内容相同的变量是相等的
l1 = ['cat', 'dog', 'mose']
l2 = ['dog', 'mose', 'cat']
d1 = {'name': 'Alice', 'high': 160, 'old': 28}
d2 = {'old': 28, 'name': 'Alice', 'high': 160}
if l1 == l2:
    print('l1=l2')
elif d1 == d2:
    print('l1!=l2 but d1=d2')       # 结果输出该语句
else:
    print('l1!=l2 and d1!=d2')

# 使用for循环遍历，只能遍历key值
for i in d1:
    print(i + ' is ' + str(d1[i]))
# keys(), values(), items()为dict的方法函数，其可以起到list的作用，但是无法修改，keys，values返回包含一个list元素的1元tuple
for i in d2.items():    # i是2元的tuple，第一个元素为key，第二个元素为value
    print(i)

# get()方法，放入key返回value，若key不存在则返回第二个参数
picnicItems = {'apple': 5, 'cups': 3}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs')

# setdefault()方法可以设置一个key的默认值，只有当key不在dict中时才会使第二参数生效，不然返回原本的值
d3 = {'name': 'Pooka', 'age': 5}
if 'color' not in d3:
    d3['color'] = 'black'
# 使用setdefault()后
d3.setdefault('color', 'black')     # 相当于赋值
d3.setdefault('color', 'white')     # 该句返回值仍为black
# 对字符计数
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for i in message:
    count.setdefault(i, 0)
    count[i] = count[i] + 1

# pprint模块，pprint.pprint()使打印更简洁，按字典的形式打印, pprint.pformat() 不打印只改格式
import pprint
pprint.pprint(count)        # 等价于print(pprint.pformat(count))

