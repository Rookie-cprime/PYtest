"""
learn python string:
所谓字符串，就是由零个或多个字符组成的有限序列，
在Python程序中，如果我们把单个或多个字符用'单引号'或者"双引号"包围起来，
可以表示一个字符串。
"""
s1 = 'hello,world'
s2 = "hello,world"
s3 = """
hello,
world!
"""
print(s1,s2,s3,end=' ')

s4 = '\'hello,world!\''
s5 = '\n\\hello,world!\\\n'
s6 = '\u9a86\u660a'

print(s4,s5,s6,end='')