"""
练习5：打印杨辉三角
			1
		1		1
	1		2		1
1		3		3		1	
"""
"""
def triangle_yanghui(num=6):
    list = [[]] * num
    for row in range(len(list)):
        list[row] = [None]*(row+1)
        for col in range(len(list[row])):
            if col == 0 or row == col:
                list[row][col] = 1
            else:
                list[row][col] = list[row-1][col-1] + list[row-1][col]
            print(list[row][col],end = '\t')
        print()
    return  row+1
    
def main():
    num = int(input('please type you wanted row number'))
    triangle_yanghui(num)
"""
def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    main()

