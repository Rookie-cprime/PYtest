"""
子类在继承了父类的方法后
可以对父类已有的方法给出新的实现版本
这个动作称之为方法重写
重写我们可以让父类的同一个行为在子类中拥有不同的实现版本
这个就是多态
"""

from abc import ABCMeta,abstractmethod

class Pet(object,metaclass = ABCMeta):
    
    def __init__(self,nickname):
        self._nickname = nickname
    @abstractmethod
    def make_voice(self):
        pass

class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
    
"""
在上面的代码中，我们将Pet类处理成了一个抽象类
所谓抽象类就是不能够创建对象的类
这种类的存在就是专门为了让其他类去继承它
但是我们可以通过abc模块的ABCMeta元类
和abstractmethod包装器来达到抽象类的效果
如果一个类中存在抽象方法那么这个类就不能够实例化
"""