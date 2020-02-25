"""
打印个怪金字塔
"""
row_num = int(input('请输入一个正整数:'))
for i in range(row_num):
    for _ in range(i+1):
        print('*',end='')#从这个例程了解了python是会自动换行的，并且'_'用的好
    for _ in range(row_num - i-1):
        print(' ',end='')
    print()
print()
for i in range(row_num):
    for _ in range(row_num-i-1):
        print(' ',end='')
    for _ in range(i+1):
        print('*',end='')
    print()
print()
for i in range(row_num):
    for _ in range(row_num-i-1):
        print(' ',end='')
    for _ in range(2*i+1):
        print('*',end='')
    print()
