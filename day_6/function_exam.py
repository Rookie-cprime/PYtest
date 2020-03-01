"""
this code to learn 'def' the function of python
"""
from random import randint

def roll_dice(n=2):
#摇骰子
    for _ in range(n):
        total+=randint(1,6)
    return  total
    
def add(a=0,b=0,c=0):
   return a+b+c

#如果没有指定参数，那么默认使用两个筛子
print(roll_dice())
#摇三个色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))
#还可不按顺序来
print(add(c=50,a=100,b=200))

