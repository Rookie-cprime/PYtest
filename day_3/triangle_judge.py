"""
这个程序用于判断三边是否构成三角形
若构成，就输出面积和周长
"""

a = float(input('输入一边的边长：'))
b = float(input('输入第二边的边长：'))
c = float(input('输入第三边的边长：'))

if (a + b) > c and (a + c) > b and (b + c) > a:
    p = (a + b + c)/2
    area = (p*(p-a)*(p-b)*(p-c))**0.5
    print('the perimeter is %f'%(a+b+c))
    print('the area of the triangle is %f'%(area))
else :
    print('this is not triangle :>')