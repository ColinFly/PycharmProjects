#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
面向对象编程
面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，
一个对象包含了数据和操作数据的函数。

面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。
为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。


而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，
并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。


在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。
自定义的对象数据类型就是面向对象中的类（Class）的概念。

面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。

小结:
数据封装、继承和多态是面向对象的三大特点，我们后面会详细讲解。
'''

#面向过程的实现方式
import types

std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }

def print_score(std):
    print('%s: %s' % (std['name'], std['score']))
print_score(std1)
print_score(std2)

#面向对象的实现方式
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print('%s:%s' % (self.name,self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

'''
##6.1类和实例
定义类通过class关键字
class Student(object):
object表示Student从object继承过来，是所有类的基类

通过特殊的init方法可以将模板属性强制填写
于是类似构造函数的东西出现了:self代表实例本身，就是java里的this
有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
但self不需要传，Python解释器自己会把实例变量传进去：
def __init__(self,name,score):


和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，
并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，
你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

'''

'''
##6.1访问限制
将类的属性私有化:如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__

'''
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

std1=Student('Colin',100)
#已经访问不了了
# std1.__name

'''
##6.2继承和多态
继承和多态是依赖关系，有继承才有多态

新增一个Animal的子类，不必对run()做任何修改，实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，
原因就在于多态。

多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，
然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，
就会自动调用实际类型的run()方法，这就是多态的意思：


对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，
而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，
这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，
只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：

对扩展开放：允许新增Animal子类；

对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。


- 静态语言 vs 动态语言
对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，
否则，将无法调用run()方法。

对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：

class Timer(object):
    def run(self):
        print('Start...')
        
这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，
那它就可以被看做是鸭子。

继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，
也可以把父类不适合的方法覆盖重写。

动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

'''


class Animal(object):
    def run(self):
        print("Animal is Running")

class Dog(Animal):
    pass

class Cat(Animal):
    def run(self):
        print('Cat is Running')

Animal().run()
Dog().run()
Cat().run()



'''
##6.3 获取对象信息
- 使用type(),返回的是对应的Class类型

- 使用isinstance():对于class的继承关系来说，使type很不方便

- 使用dir()获得一个对象的所有属性和方法,它返回一个包含字符串的list
仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
'''


print(type(123))
print(type('123'))
print(type(None))
print(type(Animal()))


print(type(123)==type(222))

def fn():
    pass

#使用types里面的常量判断一个对象是否是函数
print(type(fn)==types.FunctionType)
print(type(abs))
print(type(abs)==types.BuiltinFunctionType)

a=Animal()
d=Dog()
print(isinstance(d,Animal))
print(isinstance(a,Dog))
#还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print(isinstance((1, 2, 3), (list, tuple)))

#能用type()判断的基本类型也可以用isinstance()判断：
print(isinstance('a', str))


print(dir(a))

'''
类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，
它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
'''
print(len('ABC'))
# 是等价的
print('ABC'.__len__())



class MyObj(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x

obj=MyObj()

#比java的反射好用多了
print(hasattr(obj,'x'))
print(hasattr(obj,'y'))
print(setattr(obj,'y',19))
print(hasattr(obj,'y'))
print(getattr(obj,'y'))
#获取对象的方法
print(hasattr(obj,'power'))
p=getattr(obj,'power')
print(p)
#调用对象的方法
print(p())

#正确的用法
'''
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
'''

'''
##6.4实例属性和类属性(静态变量)
由于Python是动态语言，根据类创建的实例可以任意绑定属性。

给实例绑定属性的方法是通过实例变量，或者通过self变量：

class Student(object):
    def __init__(self, name):
        self.name = name

但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：

class Student(object):
    name = 'Student'
    
    
'''

class Student(object):
     name = 'Student'
s = Student()
print(s.name)