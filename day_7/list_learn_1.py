"""
下面的代码演示了如何向列表中添加元素以及如何从列表中移除元素
"""
# 添加元素
list1 = [1,3,5,7,9]
list1.append(200)
list1.insert(1,400)#1 position 400 value
# 合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]
print(list1)# [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1)# [1, 400, 5, 7, 100, 200, 1000, 2000]
# 从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1)-1)
print(list1)# [400, 5, 7, 100, 200, 1000]
# 清空列表元素
list1.clear()
print(list1)
list1.del