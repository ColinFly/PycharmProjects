#!/usr/bin/env python3
# -*- coding: utf-8 -*-


' a test module '

__author__ = 'Colin Lee'


'''模块
在Python中，一个.py文件就称之为一个模块（Module）。

##5.1使用模块
当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__
这样的效果是运行这个文件才会有输出，而import进别的模块时则不会有输出,显示调用才会有
比如 import hello   hello.test()
- 作用域
在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，
有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。

类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量
'''
import sys


def test():
    args=sys.argv
    if len(args)==1:
        print("one param",args[0])
    elif len(args)==2:
        print("two params")
    else:
        print("more params")

# 用于提供测试，测试的时候才会单独运行此模块
if __name__=='__main__':
    test()


def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

print(greeting('hehe'))


'''
##5.2安装第三方模块
- 安装常用模块
在使用Python时，我们经常需要用到很多第三方库，例如，上面提到的Pillow，以及MySQL驱动程序，Web框架Flask，
科学计算Numpy等。用pip一个一个安装费时费力，还需要考虑兼容性。我们推荐直接使用Anaconda，
这是一个基于Python的数据处理和科学计算平台，它已经内置了许多非常有用的第三方库，
我们装上Anaconda，就相当于把数十个第三方模块自动安装好了，非常简单易用。
'''