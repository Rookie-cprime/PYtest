"""
对于上面的代码，有C++、Java、C#等编程经验的程序员可能会问
我们给Student对象绑定的name和age属性到底具有怎样的访问权限（也称为可见性）
因为在很多面向对象编程语言中，我们通常会将对象的属性设置为私有的（private）或受保护的（protected），
简单的说就是不允许外界访问，而对象的方法通常都是公开的（public），
因为公开的方法就是对象能够接受的消息。
在Python中，属性和方法的访问权限只有两种，
也就是公开的和私有的，如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头
下面的代码可以验证这一点。
"""
class Test:
    def __init__(self,foo):
        self._foo = foo
    def _bar(self):
        print(self._foo)
        print('_bar')
def main():
    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    test._bar()
    # AttributeError: 'Test' object has no attribute '__bar'
    print(test._foo)
    
if __name__ == "__main__":
    main()
"""
但是，Python并没有从语法上严格保证私有属性或方法的私密性
它只是给私有的属性和方法换了一个名字来妨碍对它们的访问
事实上如果你知道更换名字的规则仍然可以访问到它们
下面的代码就可以验证这一点
  
class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()
"""