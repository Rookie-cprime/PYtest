"""
input函数例程
int函数例程
以及print输出占位符例程
"""

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d'%(a,b,a+b))
print(a // b)
#地板除指，除数取整数
print('%d // %d =%d'%(a,b,a//b))
print('%d %% %d = %d'%(a,b,a%b))
print('%d ** %d = %d'%(a,b,a**b))
