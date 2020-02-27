"""
寻找水仙花数
水仙花数指一个3位数，
该数字每个位上数字的立方之和
正好等于它本身
"""

for i in range(100,1000):
    low = i%10
    high = i//100
    mid = (i//10)%10
    if (low**3 + high**3 + mid**3) == i:
        print(i,end = '\t')