"""
和字符串一样，列表也可以做切片操作
通过切片操作我们可以实现对列表的复制
或者将列表中的一部分取出来创建出新的列表，
代码如下所示
"""
fruits = ['grape','apple','strawberry','waxberry']
fruits += ['pitaya', 'pear', 'mango'] 
## 列表切片
fruits2 = fruits[1:4]
print(fruits2)
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fuits3)
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5) # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']