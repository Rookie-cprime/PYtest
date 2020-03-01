"""
我们可以使用+运算符来实现字符串的拼接
可以使用*运算符来重复一个字符串的内容
可以使用in和not in来判断一个字符串是否包含另外一个字符串（成员运算）
我们也可以用[]和[:]运算符从字符串取出某个字符或某些字符（切片运算），
代码如下所示
"""
s1 = 'hello'*3
print(s1)
s2 = 'world'
s1+=s2
print(s1)#hello hello hello world
print('ll' in s1)#True
print('good' in s1)#False
str2 = 'abc123456'
#从字符串中取出指定位置的字符(下标运算)
print(str2[2])#c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5]) # c12
print(str2[2:]) # c123456
print(str2[2::2]) # c246
print(str2[::2]) # ac246
print(str2[::-1]) # 654321cba
print(str2[-3:-1]) # 45