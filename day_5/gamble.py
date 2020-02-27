"""
CRAPS又称花旗骰，
是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续要骰子，直到分出胜负。
"""
from random import randint

money = 1000
while money > 0:
    print('你现在的资产为：%d'%(money))
    debt = int(input('please put you chip'))
    go_on = False
    while True:
        num = randint(1,6) + randint(1,6)
        print('this round number is %d'%(num)) 
        if(num == 7 or num == 11):
            money = money + debt
            print('this round you win')
            break
        elif(num == 2 or num == 3 or num == 12):
            money -= debt
            print('pity you lost this round')
            break
        else:
            go_on = True
            break
    while go_on:
        print('please add you chip to follow next round or you will lost half of you chip and give up')
        add_debt = int(input('please put you chip'))
        debt += add_debt
        if(add_debt == 0):
            money = money - debt//2
            print('nice choice,this round you give up')
            break
        else:
            num_next = randint(1,6) + randint(1,6)
            print('this round number is %d'%(num_next)) 
            if(num_next == num):
                money = money + debt
                print('this round you win')
                go_on = False
            elif(num_next == 7):
                money = money - debt
                print('pity you lost this round')
                go_on = False 
            else:
                go_on = True
print('oh no you lost all your money')