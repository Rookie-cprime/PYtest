"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""

from abc import ABCMeta,abstractmethod

class Employee(object,metaclass=ABCMeta):
    def __init__(self,name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @abstractmethod
    def get_salary(self):
        pass
        
class Manager(Employee):
    def get_salary(self):
        return  15000.0
        
class Programmer(Employee):
    def __init__(self,name,working_hour = 0):
        super().__init__(name)
        self._working_hour = working_hour
    
    @property
    def working_hour(self):
        return self._working_hour
        
    @working_hour.setter
    def working_hour(self,working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0
    
    def get_salary(self):
        return 150*self._working_hour

class Salesman(Employee):
    def __init__(self,name,sale_money=0):
        super().__init__(name)
        self._sale_money = sale_money

    @property
    def sale_money(self):
        return self._sale_money
        
    @sale_money.setter
    def sale_money(self,sale_money):
        self._sale_money = sale_money if sale_money > 0 else 0
    
    def get_salary(self):
        return 1200.0 + 0.05*self._sale_money   

def main():
    emp = [
        Manager('刘备'), Programmer('诸葛亮'),
        Manager('曹操'), Salesman('荀彧'),
        Salesman('吕布'), Programmer('张辽'),
        Programmer('赵云')]
    
    for emp in emps:
        if isinstance(emp,Programmer):
            emp.working_hour = int(input('please input %s woking hours'%(emp.name)))
        elif isinstance(emp,Salesman)
            emp.sale_money = int(input('please input %s sale number'%(emp.name)))
        
        salary = str(emp.get_salary())
        print('%s本月工资为: ￥%s元' %(emp.name,salary))

if __name__ == '__main__':
    main()
        
     
