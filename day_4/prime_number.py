"""
判断一个数是不是素数
素数指的是只能被1和自身整除的大于1的整数。
"""
from math import sqrt   #从math对象中导入sqrt

x = int(input('请输入一个正整数：'))
end = int(sqrt(x))
is_prime = True
for i in range(2,end+1):
    if x%i == 0:
        is_prime = False
        break
if is_prime == True and x != 1 and x != 0:
    print('%d是素数'%(x))
else :
    print('%d不是素数'%(x))