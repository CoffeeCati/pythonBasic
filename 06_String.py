# print中添加r可以让转义字符失效，但不会因未转义导致可能提前停止输出的问题，如转义\', \''失败，并不会让后续字符串无效
print(r'hello world\n i\'m lihua')

# '''或"""即连续的3个单引号或双引号，会使得之间的所有字符都被输出，包括空格,转义字符,单双引号
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely
Bob''')
