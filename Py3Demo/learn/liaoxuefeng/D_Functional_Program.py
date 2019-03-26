#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''函数式编程
函数就是面向过程的程序设计的基本单元

而函数式编程（请注意多了一个“式”字）——Functional Programming，虽然也可以归结到面向过程的程序设计，
但其思想更接近数学计算。

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。
'''
from functools import reduce

import functools

'''
##4.1高阶函数
- 高阶函数:变量可以指向函数(函数本身可以赋值给变量)
- 函数名也是变量
- 传入函数
既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。


函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
'''

#<built-in function abs>
print(abs)

f=abs
print(abs)
print(f)

def add(x, y, f):
    return f(x) + f(y)

#直接将函数作为参数传入了amazing!!!
print(add(-5,-6,abs))

'''
##4.1.1 map和reduce函数
- map:接收两个参数,一个函数一个Iterable,将传入的函数依次作用于每个元素
- reduce:这个必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
'''

def f(x):
    return  x*x

#一眼就知道是想求每个元素的平方
r=map(f,[1,2,3,4,5])
print(list(r))
#for循环也可以,但是没有上面好
L=[]
for n in [1,2,3,4,5]:
    L.append(f(n))
print(L)

def add(x,y):
    return x+y


#累积求和
L=[1,3,5,7,9]

print(reduce(add,L))

#将序列转化为整数
def fn(x,y):
    return x*10+y

print(reduce(fn,L))

#将字符化为整数
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn, map(char2num, '13579')))


#整理一下可以写成这样,函数里面套函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

#int()函数基本也是这么实现的
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
#lambda还可以这么写
# return reduce(lambda x, y: x * 10 + y, map(char2num, s))

#练习1:
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
    # 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normalize(name):
    return name.capitalize()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

'''
##4.1.2 filter
内建函数,用于过滤序列
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。

注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，
需要用list()函数获得所有结果并返回list。

'''

# 在一个list中，删掉偶数，只保留奇数，可以这么写：

def is_odd(n):
    return n%2==1
print(list(filter(is_odd,[1,2,3,6,9])))

#删除空的字符串
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


#用filter求素数
# 1.用Python来实现这个算法，可以先构造一个从3开始的奇数序列：
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
# 注意这是一个生成器，并且是一个无限序列。
# 2.然后定义一个筛选函数：
def _not_divisible(n):
    return lambda x: x % n > 0
#3.最后，定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件
# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

#注意到Iterator是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁。


'''
##4.1.3 sorted
排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
最重要的就是实现key=的函数,(作用与每个列表中的元素)
'''
name=['bob', 'about', 'Zoo', 'Credit']
print(sorted(name))
#忽略大小写:
print(sorted(name, key=str.lower))
#逆序排列
print(sorted(name, key=str.lower,reverse=True))


#请用sorted()对上述列表分别按名字排序：(得取出元素来)
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()

def by_score(s):
    return s[1]

L2 = sorted(L, key=by_name)
print(L2)
L2 = sorted(L, key=by_score,reverse=True)
print(L2)

'''
##4.2 返回函数
- 一个函数可以返回一个计算结果，也可以返回一个函数
返回函数的时候，牢记该函数并未执行，返回函数中不要引用任何可能会变化的量
- 闭包
注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后
，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
闭包的程序结构拥有极大的威力

'''
#一般情况下的可变参求和
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
#不需要立马求和的
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum#返回的是一个对象,而不是一个结果
f=lazy_sum(1,2,3,4,5)
print(f)
print(f())
'''
在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力

请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：

>>> f1 = lazy_sum(1, 3, 5, 7, 9)
>>> f2 = lazy_sum(1, 3, 5, 7, 9)
>>> f1==f2
False

f1()和f2()的调用结果互不影响。
'''


'''
##4.3 匿名函数
lambda x:x*x 是匿名函数的写法，关键字lamda表示匿名参数，冒号前面的x表示函数参数
1.匿名函数的限制是只能有一个表达式,不用写return,表达式就是返回的结果
2.也可以将匿名函数赋给一个变量
3.也可以作为一个返回值返回

'''

f=lambda x:x*x
print(f)

def build(x,y):
    return lambda :x*x+y*y

'''
##4.4 装饰器

在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
本质上，decorator就是一个返回函数的高阶函数

总结:
在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，
而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，
也可以用类实现。

'''

#传入函数，返回函数就是装饰器模式
def log(func):
    def wrapper(*args,**kwargs):
        print('call %s():' % func.__name__)
        return func(*args,**kwargs)
    return wrapper


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。
# 比如，要自定义log的文本：
def log(text):
    def decorator(func):
        # 因为返回的那个wrapper()
        # 函数名字就是
        # 'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()
        # 函数中，否则，有些依赖函数签名的代码执行就会出错。
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator

#动态增加log功能而不改变now函数
@log('execute')
def now():
    print('2019-3-26')



#将函数赋值给变量，通过变量也能调用函数
f=now
print(f())
#函数对象都有的属性
print(now.__name__)
print(f.__name__)
now()
print(now.__name__)






'''
##4.5 偏函数
简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
返回一个新的函数，调用这个新函数会更简单。

小结:
当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
'''

print(int('12345'))
#可以接收一个base参数，可传2,8,16进制,默认10进制，现在想默认2进制
print(int('12345'))

#于是我们定义个函数:
# def int2(x,base=2):
#     return int(x,base)

#当然我们可以更简洁
int2=functools.partial(int,base=2)

print(int2('1010'))

