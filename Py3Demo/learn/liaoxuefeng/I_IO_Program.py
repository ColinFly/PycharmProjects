#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
IO编程
程序和运行时的数据是在内存中驻留，由CPU来执行,涉及到数据交换的地方，通常是磁盘和网络，就需要IO口

IO编程中,流是一个很重要的概念，可以想象成一个水管，数据就是水管里的水，
但是只能单向流动,Input Stream就是数据从外面（磁盘、网络）流进内存，
Output Stream就是数据从内存流到外面去。对于浏览网页来说，
浏览器和新浪服务器之间至少需要建立两根水管，才可以既能发数据，又能收数据。

由于CPU和内存的速度远远高于外设的速度，所以，在IO编程中，就存在速度严重不匹配的问题。
举个例子来说，比如要把100M的数据写入磁盘，CPU输出100M的数据只需要0.01秒，
可是磁盘要接收这100M数据可能需要10秒，怎么办呢？有两种办法：

第一种是CPU等着，也就是程序暂停执行后续代码，等100M的数据在10秒后写入磁盘，再接着往下执行，这种模式称为同步IO；

另一种方法是CPU不等待，只是告诉磁盘，“您老慢慢写，不着急，我接着干别的事去了”，
于是，后续代码可以立刻接着执行，这种模式称为异步IO。

很明显，使用异步IO来编写程序性能会远远高于同步IO，但是异步IO的缺点是编程模型复杂。
想想看，你得知道什么时候通知你“汉堡做好了”，而通知你的方法也各不相同。
如果是服务员跑过来找到你，这是回调模式，如果服务员发短信通知你，你就得不停地检查手机，这是轮询模式。
总之，异步IO的复杂度远远高于同步IO。
##

'''
import json
from io import StringIO, BytesIO

import os

import pickle

'''
##9.1文件读写
读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。

读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，
现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。
- 读文件(文本文件)uft8
- 二进制文件(图片视频)用rb模式打开
- 字符编码(非utf8的要传参)
    f = open('/Users/michael/gbk.txt', 'r', encoding='gbk').read
遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
- 写文件(w是覆盖,a是追加)
    with open('/Users/michael/test.txt', 'w') as f:
        f.write('Hello, world!')

'''
#读文件 打开文件,读，关闭文件

#由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
# 所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：

def readFile():
    try:
        f = open('/path/to/file', 'r')
        print(f.read())
    finally:
        if f:
            f.close()


#但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
def readFile2():
    with open('/path/to/file', 'r') as f:
        print(f.read())


#调用read()会一次性读取文件的全部内容，如果文件很大，内存就爆了，所以保险起见，可以反复调用read(size)方法
#最多读多少个字节
#readline()可以每次读取一行
#readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。


#如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；
# 如果是配置文件，调用readlines()最方便：
def readConfig():
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉


'''
##9.2StringIO和ByteIO
很多时候，数据读写不一定是文件，也可以在内存中读写。
- StringIO:只能在内存中操作String
- ByteIO:操作二进制

'''
file=StringIO()
file.write('hello')
file.write('  ')
file.write('world')
print(file.getvalue())

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
file=StringIO('Hello\nHi\nGoodbye')
while True:
    s=file.readline()
    if s== '':
        break
    print(s.strip())

file=BytesIO()
#写入的是经过utf-8编码过的bytes
file.write('中文'.encode('utf-8'))
print(file.getvalue())

# 和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
file = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(file.read())
'''
##9.3操作文件和目录
Python内置的os模块也可以直接调用操作系统提供的接口函数。
- 环境变量
'''
#posix说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.name)
#注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
print(os.uname())
#系统的环境变量
print(os.environ)
#要获取某个环境变量的值，可以调用os.environ.get('key')：
print(os.environ.get('PATH'))
#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。
#查看当前目录的绝对路径
print(os.path.abspath('.'))
path=os.path.join(os.path.abspath('.'),'testDir')
# os.mkdir(path)
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数
print(os.path.split('/Users/michael/testdir/file.txt'))
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
print(os.path.splitext('/path/to/file.txt'))
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
#复制文件的接口不在os模块而在shutil
#列出所有的目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
#列出所有的py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])



'''
##9.4序列化
我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为
serialization，marshalling，flattening等等，都是一个意思。
序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

Python提供了pickle模块来实现序列化。

- Json
如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，
但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，
也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

- Json进阶:序列化一个类

'''
# 首先，我们尝试把一个对象序列化并写入文件：

d=dict(name='Bob',age=19,score=88)
#pickl.dumps方法可以把任意对象序列化为一个bytes,然后，就可以把这个bytes写入文件
print(pickle.dumps(d))
#写入文件
file=open('dump.txt','wb')
#注意这里是dump
pickle.dump(d,file)
file.close()

#读回对象
file=open('dump.txt','rb')
d=pickle.load(file)
file.close()
# 当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。
print(d)


#Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
# 因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。


#Python对象--Json对象
jsonStr=json.dumps(d)
print(jsonStr)

#Json对象－Python对象
py=json.loads(jsonStr)
print(py)


class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

bob=Student('Bob',20,90)
#TypeError: Object of type Student is not JSON serializable
#是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
# print(json.dumps(bob))

#需要为Student专门写一个转换函数，再把函数传进去即可
def studentTodict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }

print(json.dumps(bob,default=studentTodict))

#不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
print(json.dumps(bob, default=lambda obj: obj.__dict__))


# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 23, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))


obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)