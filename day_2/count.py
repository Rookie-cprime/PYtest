"""
这个程序用于计算圆的周长
和面积
"""
import math
r = float(input('圆的半径等于： '))
l = 2 * math.pi * r
a = math.pi*r*r
print('圆的周长 = %f,圆的面积 = %f'%(l,a))
