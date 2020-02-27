"""
this code to complete
invert a positive integer
like 12345 to 54321
"""
num = int(input('please type a positive integer: '))
reverse_num = 0
while num > 0:
    reverse_num = reverse_num*10 + num%10
    num //= 10
print('the result is %d'%(reverse_num))