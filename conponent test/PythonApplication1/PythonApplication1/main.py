import random
import time
import numpy as np
from PIL import Image,ImageDraw
from equal import*

"""
这个代码主要用于测试
基于游程开发的连通域搜寻
"""
time_start  =   time.time()
e = equal()
#设计一个元组以显示标记色彩
LabelColor = ((66, 55, 255), (55, 177, 211), (33, 144, 33), (211, 122, 66), (177, 199, 44), (255, 111, 177),(11, 211, 99), (122, 22, 119),
              (166, 155, 55), (155, 77, 211), (133, 44, 33), (211, 122, 166), (177, 99, 144), (55, 111, 177),(11, 11, 99), (22, 122, 199))
TestBMP = '1.bmp'
img = np.array(Image.open(TestBMP))
#用来记录奇数行的团
A_odd_row = [[]]        #[[Xmin,Xmax,label,ccflag]]
#用来记录偶数行的团
A_even_row = [[]]       #[[Xmin,Xmax,label,ccflag]]
#用来记录整体的团
total_group = [[]]      #[[Xmin,Xmax,label,row]]
#用来存储输出的label值
already_output = []

colors = {}#用来存储Label对应的颜色
width,height = img.size


"""
def main():
    for i in range(height):
"""
def edge_start(a,b):
    """
    this function used to judge
    the group's start flag
    a is the pre pixel
    b is the curren pixel
    """
    if a == 0 and b == 1:
        return True
    else:
        return False

def edge_end(a,b):
    """
    this function used to judge
    the group's end flag
    a is the pre pixel
    b is the curren pixel
    """
    if a == 1 and b == 0:
        return True
    else:
        return False

def row_scan(line = 1,label = 1,wd = width,row = [],pre_group = [[]]):
    """
    this function to
    scan the first row
    """
    row_temp = [[]]
    temp_group = []#this group store the temp group
    scan_flag = False
    if line == 0:#第一行无需进行上述行的团扫描
        for j in range(wd):
            if args[j] == 1 and j == 0:
                temp_group[0] = j
                scan_flag = True
            elif edge_start(row[j-1],row[j])and (not scan_flag):
                temp_group[0] = j
                scan_flag = True
            elif edge_end(row[j-1],row[j]) and scan_flag:
                temp_group[1] = j-1
                temp_group[2] = e.newlabel(temp_group[1]-temp_group[0] + 1)  #如果是第一行，则赋予一个新的临时标签
                temp_group[3] = False       #初始化连通情况为无
                row_temp.append(temp_group)
                scan_flag = False
            elif scan_flag and j == wd - 1 :#如果到最后都没有结束，则强制结束
                temp_group[1] = j-1
                temp_group[2] = e.newlabel(temp_group[1]-temp_group[0] + 1)
                temp_group[3] = False
                row_temp.append(temp_group)
                scan_flag = False
    else:#除第一行外的所有行都要对之前一行扫过的团进行扫描
        for j in range(wd):
            if args[j] == 1 and j == 0:
                temp_group[0] = j
                scan_flag = True
            elif edge_start(row[j-1],row[j]) and (not scan_flag):
                temp_group[0] = j
                scan_flag = True
            elif edge_end(row[j-1],row[j]) and scan_flag :
                label_flag = True# this flag used to judge whether this group has been labeled by previous group.
                temp_group[1] = j-1
                row_actual = [[]]       #this mainly change the conect flag,used for second scan
                total_actual = [[]]     #this mainly change the conect flag
                for val in pre_group:
                    if(temp_group[0]<=val[0]+1 or temp_group[1] >= val[1]-1):#判断是否存在联通关系，采取8连通
                        if(label_flag):
                            temp_group[2] = val[2]
                            label_flag = False
                            val[3] = True   #更改联通标志位
                        else:
                            val[3] = True
                            e.union(val[2],temp_group[2]) #合并等价标签和面积
                        
                    row_actual.append(val)
                    val[3] = line
                    total_actual.append(val)
                pre_group   =   row_actual[:]               #需要把已经更新的信息更新到前行
                if label_flag:                          #如果label_flag还是True，说明与之前一行的连通并没有关系，所以需要赋给他新的标签
                    temp_group[2] = e.newlabel(temp_group[1]-temp_group[0] + 1)
                    temp_group[3] = False
                row_temp.append(temp_group)             #完成上述两步后，并入该行
                scan_flag = False
            elif j == wd-1 and scan_flag :
                label_flag = True# this flag used to judge whether this group has been labeled by previous group.
                temp_group[1] = j-1
                row_actual = [[]]       #this mainly change the conect flag,used for second scan
                total_actual = [[]]     #this mainly change the conect flag
                for val in pre_group:
                    if(temp_group[0]<=val[0]+1 or temp_group[1] >= val[1]-1):#判断是否存在联通关系，采取8连通
                        if(label_flag):
                            temp_group[2] = val[2]
                            label_flag = False
                            val[3] = True   #更改联通标志位
                        else:
                            val[3] = True
                            e.union(val[2],temp_group[2]) #合并等价标签和面积 
                    row_actual.append(val)
                    val[3] = line
                    total_actual.append(val)
                pre_group   =   row_actual[:]
                if label_flag:                          #如果label_flag还是True，说明与之前一行的连通并没有关系，所以需要赋给他新的标签
                    temp_group[2] = e.newlabel(temp_group[1]-temp_group[0] + 1)
                    temp_group[3] = False
                row_temp.append(temp_group)             #完成上述两步后，并入该行
                scan_flag = False
                    





    return (label,row_temp,row_actual,total_actual)

def sec_scan(group_1 = [[]],group_2 = [[]]):#此函数用来搜寻团中可以退出的部分
    end_group_label = []
    for val in group_1:
        if not val[3]:#如果他显示出现过与之后的团无联通关系
            for val_0 in group_2:
                end_flag = True
                if e.findroot(val_0[2]) == e.findroot(val[2]):#如果他与本行中的其他团的根源标记值相同，代表它其实并未结束
                    end_flag = False
                    break
            if(end_flag):
                end_group_label.append(e.findroot(val[2]))
    return end_group_label

def pop_out(end_group = [],total_group = [[]]):
    """
    这个函数用于搜寻团中的
    等价位置并且输出
    团本身和其等价信息
    pop_flag:记录是否
    """
    out_group = [[]]
    out_posision = []#记录其表中的位置，输出后就把total_group中的这些项剔除
    pop_flag = False
    for label in end_group:
        for i,val in enumorate(total_group):
            if(e.findroot(val[2]) == label):
                val[2] = label
                out_group.append(val)
                out_position.append(i)
                pop_flag = True

    return (out_group,out_posision,pop_flag)

def fill_group(total_group = [[]],posision = []):
    """
    这个函数用于压缩
    总团的信息
    便于FPGA的资源存储
    """
    new_total_group = [[]]
    for i,val in enumorate(total_group):
        if i not in posision:
            new_total_group.append(val)
    return new_total_group

def draw_pic(width = 0,height = 0,out_group = [[]],colors = {}):
    output_img = Image.new("RGB", (width, height))
    outdata = output_img.load()
    for val in out_group:
        component = val[2]
        if component not in colors:
            colors[component] = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
        for y in range(val[0],val[1]+1):
            outdata[y, val[3]] = colors[component]
    return (colors, output_img)


        


            



    



