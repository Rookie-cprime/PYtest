"""
可变参数在函数中
学习实例
"""

def add(*args):
    total = 0
    for val in args:
        total+=args
    return total
print(add())
print(add(1))
print(add(1,2))
print(add(3,5,7))