"""
str format
"""
#可以用下面的方式来格式化输出字符串。
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
#当然，我们也可以用字符串提供的方法来完成字符串的格式，代码如下所示。
print('{0} * {1} = {2}'.format(a,b,a*b))
