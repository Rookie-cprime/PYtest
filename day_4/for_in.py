"""
学习使用for循环求累加和
"""
t = int(input('请输入想要累加的次数:'))
sum = 0
for x in range(t+1):#可以看出这里是t+1可以推断出，x到100就停止了
    sum += x
print('the result of the %d = %d'%(t,sum))