"""
斐波那契数列（Fibonacci sequence），又称黄金分割数列，
斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和
生成斐波那契数列的前20个数
"""
one = 1
two = 1
for i in range(20):
    if(i == 0 or i == 1):
        print(1,end=',')
    else:
        num = one + two
        two = one
        one = num
        print('%d'%(num),end=',')