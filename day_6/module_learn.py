"""
Python模块化调用
不执行模块中的可执行代码
因为只有直接执行的模块的名字才是"__main__"
"""
def	 foo():
    pass
def  bar():
    pass
# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if _name_ == '_main_':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
    