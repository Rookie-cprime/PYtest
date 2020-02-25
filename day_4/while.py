"""
学习使用while循环
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
import random#调用random对象

answer = random.randint(1,100)
counter = 0
while True:#True就代表一直循环下去
    counter += 1
    number = int(input('请输入你猜的整数：'))
    if number > answer:
        print('猜大了')
    elif number < answer:
        print('猜小了')
    else :
        break#可以直接跳出本次循环，对应的continue可以直接跳过后面的循环，进入下一轮循环
print('你一共猜了%d才猜对嗷'%(counter))