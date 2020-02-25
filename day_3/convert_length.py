"""
英寸与厘米的换算
"""

value = float(input('请输入数据: '))
unit = input('请输入单位：')
if unit == 'in' or unit == '英寸':
    print('%f英寸 == %f厘米'%(value,value*2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 == %f英寸'%(value,value/2.54))
else:
    print('你输你horse的单位呢')
    
