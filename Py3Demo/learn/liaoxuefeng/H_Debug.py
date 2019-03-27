#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
##8.1错误处理
用错误码来表示是否出错十分不便，因为函数本身应该返回的正常结果和错误码混在一起，
造成调用者必须用大量的代码来判断是否出错：

def foo():
    r = some_function()
    if r==(-1):
        return (-1)
    # do something
    return r

def bar():
    r = foo()
    if r==(-1):
        print('Error')
    else:
        pass


一旦出错，还要一级一级上报，直到某个函数可以处理该错误（比如，给用户输出一个错误信息）。

所以高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外。



'''
import logging

try:
    print('tyr...')
    r=10/0
    print('result:'+r)
except ZeroDivisionError as e:
    print('exception:',e)
finally:
    print('finally')

print('END')


def foo():
    pass
try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')

# 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，
# 如果有，也被第一个except给捕获了。

# Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：

# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，
# 比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：
# 也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。
    # 这样一来，就大大减少了写try...except...finally的麻烦。


'''

##8.2调试

- 断言
assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
- logging
这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
当我们指定level=INFO时，logging.debug就不起作用了。
'''
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

# main()


s = '0'
n = int(s)
logging.basicConfig(level=logging.INFO)
logging.info('n = %d' % n)
print(10 / n)

print('hehe')

'''
##8.3单元测试
为了编写单元测试，我们需要引入Python自带的unittest模块，编写mydict_test.py如下：

    
'''

'''
##8.4文档测试
Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。
doctest非常有用，不但可以用来测试，还可以直接作为示例代码。通过某些文档生成工具，
就可以自动把包含doctest的注释提取出来。用户看文档的时候，同时也看到了doctest。
'''