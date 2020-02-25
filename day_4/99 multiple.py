"""
99乘法表
"""
for x in range(1,10):
    for y in range(1,10):
        print('%d*%d=%d'%(x,y,x*y),end='\t')
    print('\n')
