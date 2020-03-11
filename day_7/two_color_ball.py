"""
综合案例
双色球选号。
"""
from random import randint,randrange,sample

def display(balls):
   """
    输出列表中的双色球号码
   """
   for index,ball in enumerate(balls):
   #enumerate：可以同时输出序号和内容
    if index == len(balls)-1:
        print('|',end='')
    print('%02d'%(ball),end='')
   print()
   
def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1,34)]
    # another method create list
    select_balls = []
    select_balls = sample(red_balls,6)
    #sample:从序列中随机抽取6个元素组成新的序列
    select_balls.sort()
    #sort:排序
    select_balls.append(randint(1,16))
    return select_balls

def main():
    n = int(input('How many stake you want?'))
    for _ in range(n):
        display(random_select())
     
if __name__ == '__main__':
    main()     