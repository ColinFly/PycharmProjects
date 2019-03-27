#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
面向对象高级编程
数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。在Python中，面向对象还有很多高级特性，
允许我们写出非常强大的功能。

我们会讨论多重继承、定制类、元类等概念。
'''
from enum import Enum, unique
from types import MethodType

'''
##7.1使用__slots__(插槽)
正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，
这就是动态语言的灵活性。

通常情况下，上面的set_score方法可以直接定义在class中，
但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现

- 使用__slots
为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：


'''

class Student(object):
    pass

s=Student()
#给实例绑定一个属性
s.name='Colin'
print(s.name)
def set_age(self,age):
    self.age=age

#给实例绑定一个方法
s.set_age=MethodType(set_age,s)
s.set_age(25)
print(s.age)


#给类绑定一个方法
def set_score(self,score):
    self.score=score

Student.set_score=set_score

s1=Student()
s1.set_score(100)
print(s1.score)



#限制能绑定的属性
class Student(object):
    __slots__ = ('name','score')

#绑定属性age报错
s=Student()
# s.age=11

#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class GraduateStudent(Student):
     pass
g = GraduateStudent()
g.age=111

print(g.age)
#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。

'''
##7.2 使用property
既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢?

还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的

注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的


小结
@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
'''
#这样确实可以做到参数检查，但是太复杂了

class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

class Student2(object):
    #负责把一个方法变成属性调用
    @property
    def score(self):
        return self.score

    #负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s=Student2()
# s.score=111

# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

#上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。


'''

##7.3多重继承--java里的接口
通过多重继承，一个子类就可以同时获得多个父类的所有功能。

MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，
我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。

我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。

小结
由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。

只允许单一继承的语言（如Java）不能使用MixIn的设计(好像可以用接口?)。


'''


'''
##7.4定制类
- __str__:toString方法
- __iter__:使能被循环
- __getitem__:使能按照下标取元素
- __getattr__:动态返回一个属性
- __call__:任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用

'''


class Student4(object):
    def __init__(self,name):
        self.name=name

    #相当于重写string方法
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    #使调试和用户看到的一样
    __repr__=__str__


print(Student4('mm'))



# 以斐波那契数列为例，写一个Fib类，可以作用于for循环：

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
for n in Fib():
    print(n)





# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
#如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。

# 利用完全动态的__getattr__，我们可以写出一个链式调用：

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__
#找不到属性所以动态格式化字符串,这是java做不到的,因为通不过编译
i=Chain().status.user.timeline.list
print(i)


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
s()
# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，
# 把函数看成对象，因为这两者之间本来就没啥根本的区别。

'''
##7.5使用枚举类

Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
'''

Month=Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

#value属性则是自动赋给成员的int常量，默认从1开始计数。
for name,member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

#unique可以帮我们检查有没有重复值
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Mon)
print(Weekday.Mon.name)
print(Weekday.Mon.value)
print(Weekday(1))


'''
##7.5使用元类
metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，
你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。

动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？正常情况下，确实应该直接写，通过metaclass修改纯属变态。

但是，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。

ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。

要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
'''