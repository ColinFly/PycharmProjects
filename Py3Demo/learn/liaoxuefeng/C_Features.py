#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
高级特性
##3.1 切片
    用来操作list或tupple
    左闭右开
    在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring），
    其实目的就是对字符串切片。Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单
'''

L = list(range(100))
print(L)
# 取前10个元素
print(L[0:10])

# 取后1个
print(L[-1])

# 取后10个
print(L[-10:])

# 前10-20
print(L[10:20])
# 前10个数,每两个取一个
print(L[0:10:2])
# 所有数,每5个取一个
print(L[::5])
# 复制一个数组
print(L[:])

# 对于tuple
T = (1, 2, 3, 4)
print(T[0:3])
# 字符串也可以看做是list
S = 'ABCDEFG'
print(S[:3])

'''
##3.2　迭代
如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。



'''
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for key in 'ABC':
    print(key)

from collections import Iterable, Iterator

# 检查dict是否可迭代
print(isinstance(d, Iterable))
# 检查list是否可迭代
print(isinstance([1, 2, 3], Iterable))
# 检查整数是否可迭代
print(isinstance(123, Iterable))

# 实现有下标的迭代
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# for循环里面可以放两个变量，java是不可以的:
for x, y in [(1, 1), (2, 2), (3, 3)]:
    print(x, y)

'''
##3.3　列表生成式
List Comprehensions
是Python内置的非常简单却强大的可以用来创建list的生成式。

'''

# 用循环实现，
# 需要两行代码，java也是这样实现
L = []
for x in range(1, 11):
    L.append(x * x)

print(L)

# 用列表生成式来实现,一行即可
L2 = [x * x for x in range(1, 11)]
print(L2)

# 筛选出偶数的平方
# 操作--生成--条件
L3 = [x * x for x in range(1, 11) if x % 2 == 0]
print(L3)

# 遍历dict
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, v)

# 用列表生成式
L4 = [k + ':' + v for k, v in d.items()]
print(L4)

# 把列表中的所有字母变成小写
L5 = ['Hello', 'World', 18, 'IBM', 'Apple']
print([x.lower() for x in L5 if (isinstance(x, str))])

'''
##3.2　生成器
生成器
阅读: 479147
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

要创建一个generator，有很多种方法。
1.第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
2.如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：

'''
# 创建生成器对象
g = (x * x for x in range(1, 11))
print(g)
# 查看对象里的元素
for k in g:
    print(k)


# 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


# print(fib(0))
# print(fib(1))
# 打印前三项
print(fib(3))


# 将上述改为生成器:
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


print(fib2(5))
# 用for循环遍历的时候注意一下必须捕获异常,
# 1.像fib2就有无限个元素所以要设置一个条件来退出循环
# 2.对于有限个元素的生成器就要捕获异常,对于.next
while True:
    try:
        x = next(g)
        print('g:' + x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# 试一下输出杨辉三角
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]

def triangles():
    L = [1]     #定义L为一个只包含一个元素的列表
    while True:
        # print(L) #len(L)将会成为变量
        yield L     #定义为生成器函数
        L = [1] + [L[n] + L[n - 1] for n in range(1, len(L))] + [1]


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
'''
解析
输出：
    第一行：L = [1]
    len(L) = 1
    range(1,1) = []    #此时， L[n-1] for n in range(1,len(L))] 这个for in 不执行
    第二行：L = [1] + [L[n] + L[n-1] for n in [] ] + [1]
            L = [1] + [1]
            L = [1, 1]

    len(L) = 2
    range(1,2) = [1]
    第三行：L = [1] + [L[n] + L[n-1] for n in [1]] + [1]
            L = [1] + [ L[1] + L[1-1] ] + [1]
            L = [1] + [ L[1] + L[0] ] + [1]
            L = [1] + [ 1 + 1] + [1]
            L = [1, 2, 1]
'''
'''
##3.2　迭代器
我们已经知道，可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str等；

一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以使用isinstance()判断一个对象是否是Iterable对象：

生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

把list、dict、str等Iterable变成Iterator可以使用iter()函数：


你可能会问，为什么list、dict、str等数据类型不是Iterator？

这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。

可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，

只有在需要返回下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

'''

print(isinstance([],Iterator))
#变成Iterator
print(isinstance(iter([]),Iterator))

