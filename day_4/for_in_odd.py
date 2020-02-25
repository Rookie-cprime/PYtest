"""
学习使用for循环求累加偶数和
"""
t = int(input('请输入想要累加偶数的次数:'))
sum = 0
for x in range(2,101,2):#可以看出这第一个是起始位，最后一项是隔次加2
    sum += x
print('the result of the %d = %d'%(t,sum))