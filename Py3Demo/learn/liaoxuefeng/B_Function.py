#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
##2.1调用函数
    熟悉一些内置函数

'''
'''
##2.2定义函数
-　定义:用def关键字,函数名和参数,如有必要则进行参数检查
- 空函数:先定义占位，不影响运行
    def nop():
        pass
- 参数检查 isinstance
- 返回多个值(实际是一个值，通过tupple实现多个值的返回，很方便)
        
'''


def my_abs(x):
    if(x>0):
        return x
    else:
        return -x

def my_abs2(x):
    #参数检查
    if not isinstance(x,(int,float)):
        return TypeError('bad type')
    if(x>0):
        return x
    else:
        return -x


print(my_abs(-2))
print(my_abs2('A'))

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

#返回一个元组
print(move(100, 100, 60, math.pi / 6))
#多个变量可以同时接收一个tuple,按位置赋给对应的值,所以超级方便
x,y=move(100, 100, 60, math.pi / 6)
print(x)
print(y)

'''
##2.3函数的参数
- 位置参数:按位置赋给参数
- 默认参数: 定义默认参数要牢记一点：默认参数必须指向不变对象！
- 可变参数 *定义,可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
- 关键字参 **定义 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
- 命名关键字参数 如果要限制关键字参数的名字，就可以用命名关键字参数 def person(name, age, *, city, job):*后面的参数被视为命名关键字参数
    命名关键字参数必须传入参数名
- 参数组合
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是：位置参数、默认参数、可变参数、命名关键字参数和关键字参数。


虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。

'''


def power(x):
    return x*x


#1.定义了这个以后,上面的函数将会失效,需要通过默认参数来兼容一个参数的调用
def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
#2.于是添加默认参
def power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(9))
print(power(9,3))


#这里的默认参是一个list-->可变哦
def add_end(L=[]):
    L.append("END")
    return L

#连续调用就会有不同的结果，这不是我们希望的
print(add_end())
print(add_end())


#修改参数为不可变对象
def add_end(L=None):
    if L is None:
        L=[]
    L.append("END")
    return L

print(add_end())
print(add_end())


#对于计算a2 + b2 + c2 + ……
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

#直接传参
print(calc(1,2,3,5))
#对于已存在一个list,可这样传参,在list前加*,就是将list化为可变参,太方便了
list=[1,2,3,4,5]
print(calc(*list))





#关键字可变参
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

person('Colin',18)

person('Adam', 45, gender='M', job='Engineer')

#命名关键字,必须传入city和job
def person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')

#args是可变参，则后面的city和job必填,只不过不用加*号(不然就没要定义出来了)
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

#命名关键字参数必须传入参数名
person('Jack', 24,33,job="Engineer",city="Hehe")

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

#必须传入一个d
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# f1(1)
f1(1,2)
f1(1,2,3)
f1(1,2,3,4)
f1(1,2,3,4,5)
f1(1,2,3,4,x=99)


f2(1,2,3,d=1)

'''
##2.4递归函数
如果一个函数在内部调用自身本身，这个函数就是递归函数。
问题:在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，
栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。

针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。


'''

#计算阶乘n! =5*4*3*2*1
def fact1(n):
    if n==1:
        return 1
    return n*fact1(n-1)
#尾递归优化
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    #仅返回递归函数本身,并不开始计算,最后再计算一次
    #尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
    return fact_iter(num - 1, num * product)
'''
fact(5)对应的fact_iter(5, 1)的调用如下
===> fact_iter(5, 1)
===> fact_iter(4, 5)
===> fact_iter(3, 20)
===> fact_iter(2, 60)
===> fact_iter(1, 120)
===> 120
'''