"""
找出10000以内的完美数
完美数又称为完全数或完备数
它的所有的真因子（即除了自身以外的因子）的和
恰好等于它本身
"""

for i in range(2,10000):
    sum = 0
    for j in range(1,i):
        if(i%j == 0):
            sum+=j
    if(sum == i):
        print('%d'%(i),end = ', ')
    