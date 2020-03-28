import random
import time
import numpy as np
from PIL import Image,ImageDraw
from equal import*

"""
这个代码主要用于测试
基于游程开发的连通域搜寻
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

def row_scan(line = 1,wd = 0,row = [],pre_group = [[]],e = Label()):
    """
    this function to
    scan the first row
    line = 当前扫描的行数
    row = 当前行内所有的像素
    pre_group为之前扫描后的行
    """
    row_temp = []
    temp_group = [0,0,0,0]#this group store the temp group
    row_actual = pre_group[:]       #this mainly change the conect flag,used for second scan
    scan_flag = False
    if line == 0:#第一行无需进行上述行的团扫描
        for j in range(wd):
            if row[j] == 1 and j == 0 and (not scan_flag):
                temp_group[0] = 0
                scan_flag = True
            elif edge_start(row[j-1],row[j])and (not scan_flag):
                temp_group[0] = j
                scan_flag = True
            elif edge_end(row[j-1],row[j]) and scan_flag:
                temp_group[1] = j-1
                area = int(temp_group[1]-temp_group[0]+1)
                temp_group[2] = e.newlabel(area)  #如果是第一行，则赋予一个新的临时标签
                temp_group[3] = False       #初始化连通情况为无
                row_temp.append(temp_group[:])
                scan_flag = False
            elif scan_flag and j == wd - 1 :#如果到最后都没有结束，则强制结束
                temp_group[1] = j
                temp_group[2] = e.newlabel(temp_group[1]-temp_group[0] + 1)
                temp_group[3] = False
                row_temp.append(temp_group[:])
                scan_flag = False
    else:#除第一行外的所有行都要对之前一行扫过的团进行扫描
        for j in range(wd):
            if row[j] == 1 and j == 0:
                temp_group[0] = j
                scan_flag = True
            elif edge_start(row[j-1],row[j]) and (not scan_flag):
                temp_group[0] = j
                scan_flag = True
            elif edge_end(row[j-1],row[j]) and scan_flag :
                label_flag = True# this flag used to judge whether this group has been labeled by previous group.
                temp_group[1] = j-1
                row_actual = []       #this mainly change the conect flag,used for second scan
                for val in pre_group:
                    if(val[1] >= temp_group[0] - 1 and val[0] <= temp_group[1] + 1):#判断是否存在联通关系，采取8连通
                        if(label_flag):
                            temp_group[2] = val[2]
                            temp_group[3] = False
                            label_flag = False
                            val[3] = True   #更改联通标志位
                        else:
                            val[3] = True
                            e.union(val[2],temp_group[2]) #合并等价标签和面积
                        
                    row_actual.append(val[:])
                if label_flag:                          #如果label_flag还是True，说明与之前一行的连通并没有关系，所以需要赋给他新的标签
                    temp_group[2] = e.newlabel(temp_group[1]-temp_group[0] + 1)
                    temp_group[3] = False
                row_temp.append(temp_group[:])             #完成上述两步后，并入该行
                scan_flag = False
            elif j == wd-1 and scan_flag :
                label_flag = True# this flag used to judge whether this group has been labeled by previous group.
                temp_group[1] = j
                row_actual = []       #this mainly change the conect flag,used for second scan
                for val in pre_group:
                    if(val[1] >= temp_group[0] - 1 and val[0] <= temp_group[1] + 1):#判断是否存在联通关系，采取8连通
                        if(label_flag):
                            temp_group[2] = val[2]
                            temp_group[3] = False
                            label_flag = False
                            val[3] = True   #更改联通标志位
                        else:
                            val[3] = True
                            e.union(val[2],temp_group[2]) #合并等价标签和面积 
                    row_actual.append(val[:])
                if label_flag:                          #如果label_flag还是True，说明与之前一行的连通并没有关系，所以需要赋给他新的标签
                    temp_group[2] = e.newlabel(temp_group[1]-temp_group[0] + 1)
                    temp_group[3] = False
                row_temp.append(temp_group[:])             #完成上述两步后，并入该行
                scan_flag = False
                    
    return (row_temp,row_actual,e)

def sec_scan(group_1 = [[]],group_2 = [[]],i = 1,e = Label()):#此函数用来搜寻团中可以退出的部分
    """
    group_1为前一行的团
    group_2为当前行的团
    """
    end_group_label = []
    total_actual    = []
    pop_flag    =   False
    for val in group_1:
        if not val[3]:#如果他显示出现过与之后的团无联通关系
            end_flag = True
            for val_0 in group_2:
                if e.findroot(val_0[2]) == e.findroot(val[2]):#如果他与本行中的其他团的根源标记值相同，代表它其实并未结束
                    end_flag = False
                    break
            if(end_flag):
                end_group_label.append(e.findroot(val[2]))
                pop_flag = True

        val_1 = val[0:3] + [i-1]
        total_actual.append(val_1[:])
    return (total_actual,end_group_label,pop_flag)

def pop_out(end_group = [],total_group = [[]],e = Label()):
    """
    这个函数用于搜寻团中的
    等价位置并且输出
    团本身和其等价信息
    pop_flag:记录是否输出
    out_group:记录输出的团组用于绘图
    out_posision:记录这些输出的位置用于压缩总团数组的存储空间
    """
    out_group = []
    out_posision = []#记录其表中的位置，输出后就把total_group中的这些项剔除
    for label in end_group:
        for i,val in enumerate(total_group):
            if(e.findroot(val[2]) == label):
                val[2] = label
                out_group.append(val)
                out_posision.append(i)

    return (out_group,out_posision)

def fill_group(total_group = [[]],posision = []):
    """
    这个函数用于压缩
    总团的信息
    便于FPGA的资源存储
    """
    new_total_group = []
    for i,val in enumerate(total_group):
        if i not in posision:
            new_total_group.append(val)
    return new_total_group

def draw_pic(out_group = [[]],colors = {},output_img = ([[]]),e = Label()):
    outdata = output_img.load()
    for val in out_group:
        component = e.findroot(val[2])
        if component not in colors:
            colors[component] = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
        for y in range(val[0],val[1]+1):
            outdata[y, val[3]] = colors[component]
    return (colors, output_img)


def main():
    time_start  =   time.time()
    e = Label()
    #设计一个元组以显示标记色彩
    TestBMP = 'test.bmp'
    img = Image.open(TestBMP)
    width,height = img.size
    data = np.array(img)
    #用来记录奇数行的团
    A_odd_row = [[]]        #[[Xmin,Xmax,label,ccflag]]
    #用来记录偶数行的团
    A_even_row = [[]]       #[[Xmin,Xmax,label,ccflag]]
    #用来记录整体的团
    total_group = []      #[[Xmin,Xmax,label,row]]
    #用来存储输出的label值
    already_output = []
    #用来存储Label对应的颜色
    colors = {}
    #用来存储标记后的图片
    output_img = Image.new("RGB", (width, height))
    print(data)
    for i in range(height):
        if i%2 == 0:
            (A_odd_row,A_even_row,e) = row_scan(i,width,data[i],A_even_row,e)
            print('第%d行：'%(i+1))
            print('当前行的团[Xmin,Xmax,label,ccflag]:',A_odd_row)
            print('更新联通标志位后的前一行团[Xmin,Xmax,label,ccflag]:',A_even_row)
            if i != 0:
                (total_actual,end_label,pop_flag) = sec_scan(A_even_row,A_odd_row,i,e)
                total_group += total_actual[:]
                print('总团数组里存的团[Xmin,Xmax,label,line]:',total_group)
                if(pop_flag):
                    (out_group,out_posision) = pop_out(end_label,total_group,e)
                    total_group = fill_group(total_group,out_posision)
                    print('经过裁剪后的总团数组里存的团[Xmin,Xmax,label,line]:',total_group)
                    (colors,output_img) == draw_pic(out_group,colors,output_img,e)
        else:
            (A_even_row,A_odd_row,e) = row_scan(i,width,data[i],A_odd_row,e)
            print('第%d行：'%(i+1))
            print('当前行的团[Xmin,Xmax,label,ccflag]:',A_even_row)
            print('更新联通标志位后的前一行团[Xmin,Xmax,label,ccflag]:',A_odd_row)
            (total_actual,end_label,pop_flag) = sec_scan(A_odd_row,A_even_row,i,e)
            total_group += total_actual[:]
            print('总团数组里存的团[Xmin,Xmax,label,line]:',total_group)
            if(pop_flag):
                (out_group,out_posision) = pop_out(end_label,total_group,e)
                total_group = fill_group(total_group,out_posision)
                print('经过裁剪后的总团数组里存的团[Xmin,Xmax,label,line]:',total_group)
                (colors,output_img) == draw_pic(out_group,colors,output_img,e)
        if (i == 9):
            (colors,output_img) == draw_pic(total_group,colors,output_img,e)
           
    output_img.show()

if __name__ == '__main__':
    main()
            



    



