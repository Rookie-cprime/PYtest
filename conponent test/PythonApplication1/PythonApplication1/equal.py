"""
这个类主要用于连通域搜寻存储等价
标记
"""
class Label:
    def __init__(self):
        self.P = [0]     #this is the equal label store the address is current label,the value inside is the true label
        self.A = [0]     #this is to calculate the area
        self.label = 1
    def newlabel(self,area = 1):
       """
       this function to create a new label
       when to group area is not 1
       """
       r = self.label
       self.label+=1
       self.P.append(r)
       self.A.append(area)
       return r
    def findroot(self,current_label):
       """
       this i means the current label
       """
       i = current_label       
       while self.P[i] < i:
            i  = self.P[i]
       root = self.P[i]
       return root
    def add_area(self,label,area):
        i = findroot(label)
        self.A[i] += area

    def changeroot(self,current_label,new_root):
        """
        this function mainly used to change the relation between two labels
        """
        i = current_label
        root = new_root
        while self.P[i] < i:
            j = self.P[i]
            self.P[i] = root
            i = j
        self.P[i] = root
        self.A[root] = self.A[root]+self.A[i]

    def union(self,current_label_pre,curent_label_now):
        if(current_label_pre!=curent_label_now):
            root1 = findroot(current_label_pre)
            root2 = findroot(current_label_now)
            if root1 > root2:
                changeroot(current_label_pre,root2)
                add_area(root2,self.A[root1])
            elif root1 < root2:
                changeroot(current_label_now,root1)
                add_area(root1,self.A[root2])
    
    def flatten(self):#只是一次简单的压缩，主要是优化代码运算速度，也可以不做这步
        for i in range(1, len(self.P)):
            self.P[i] = self.P[self.P[i]]
    
        