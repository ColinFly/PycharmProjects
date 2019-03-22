#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
##1.1数据类型和常量
- 数据类型
    整数,浮点数(小数),字符串(单引号和双引号没啥区别),布尔值(True和False,用and,or,not来运算),空值:None
- 变量
    无需指定类型(动态语言)
- 常量
    大写，没有机制保证不去改变它
- 两种除法
    /:浮点数计算
    //:地板除,结果是整数
    Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf
'''

print('hello \nworld')
print(r'''hello,\n world''')

# 一般除法
print(10 / 3)
# 地板除
print(10 // 3)
# 取余
print(10 % 3)

'''
##1.2字符串和编码
- 字符编码
ASCII(最开始的老美,1个字节搞定)-->GB2312(加入中文,一般两个字节，复杂的4个,和其它语言有冲突)-->Unicode(万国码,两个字节,英文不划算)
-->UTF-8(可变长编码,UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节)
字符	    ASCII	    Unicode	    UTF-8
A	    01000001	00000000    0100000101000001
中	    	        01001110    0010110111100100 10111000 10101101
从上面的表格还可以发现，UTF-8编码有一个额外的好处，就是ASCII编码实际上可以被看成是UTF-8编码的一部分，
所以，大量只支持ASCII编码的历史遗留软件可以在UTF-8编码下继续工作

Window记事本:文件的utf-8读到内存变为unicode,编辑完成后,转换为utf-8保存到文件
浏览器:服务器的unicode编码会转化为utf-8在传到浏览器,所以你看到很多网页的源码上会有类似<meta charset="UTF-8" />的信息，表示该网页正是用的UTF-8编码。
- Python字符串
py3中，字符串是unicode编码的
对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x=b'ABC'
要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。字符的就可能不止一个字节了(中文)
反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：

由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

- 字符格式化
1.在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：
'亲爱的xxx你好！你xx月的话费是xx，余额是xx'之类的字符串，而xxx的内容都是根据变量变化的，所以，需要一种简便的格式化字符串的方式。
2.format()
另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：

请牢记仅使用UTF-8编码


'''

# 65
print(ord('A'))
# 20013
print(ord('中'))
# B
print(chr(66))
# 文
(chr(25991))
# 字符的整数编码(16进制)
print('\u4e2d\u6587')

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# 显然会报错，因为1个字节装不下
# print('中文'.encode('ascii'))

# byte解码为utf-8
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(b'ABC'.decode('ascii'))

# 可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。
print(len('A'))
print(len(b'ABC'))
print(len('中'.encode('utf-8')))

# '亲爱的xxx你好！你xx月的话费是xx，余额是xx'
print('Hi,大斌 %s, you have $%d.' % ('Michael', 1000000))
print('亲爱的%s,你%d月分的话费是%.2f' % ('大斌', 2, 11.090009))
# 'growth rate: %d %%' % 7
print('growth rate: %d %%' % 7)
# 传入的参数依次替换字符串内的占位符{0}、{1}
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

'''
##1.3使用list和tuple
- list
    1.有序的集合，可添加和删除元素
    2,可用索引来访问,负值代表从后面开始访问
    3.插入用insert,append,删除用pop,替换就直接赋值
    4.里面的元素可以是不同类型，也可以包含另一个list
- tupple(元组)
    1.初始化后就不过修改,指向不变，内部元素可以变化
    2.可以像list一样访问元素，但不能insert和append了
    3.定义的时候元素就必须确定下来，(),(2,),(1,2,3)为了避免和赋值的小括号一样，一个元素必须有逗号
    4.正确的使用方式是tupple里面的元素也不能变化,才能写出安全的代码
    
'''

list = ['Apple', 123, True]
print(list[-1])

list.append("Colin")
print(list)

list2 = ["AAAA", 9999]
list.insert(3, list2)
print(list)
list.pop()
print(list)
print(list[3][1])

classmates = ('Michael',)

print(classmates)

'''
##1.4条件判断
- if..elif.else
- input


'''

age = 20
if age > 18:
    print('adult')

age = 3
if age > 18:
    print('adult')
else:
    print('child')

age = 17
if age > 18:
    print('adult')
elif age > 16:
    print('teen')
else:
    print('child')

# 读取用户输入
# birth=input('birth:')
# birth=int(birth)
# if birth<2000:
#    print('90后')
# else:
#    print('00后')


'''
##1.5循环
- for 
- while
- break　跳出循环
- continue 跳过这次循环，继续下次循环

   
'''

sum = 0
# 用list(range(11))函数
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in list1:
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n=n-2
print(sum)


n=1
while n<100:
    if n>10:
        print('Break')
        break
    n=n+2
print('END')


#要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，
# 上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)


'''
##1.6使用dict和set
- dict
    1.就是java里的map,键值对，极其方便查找,可以放不同类型的，比java方便多了
    2.需要占用大量内存，浪费
    3.键必须用不可变对象(字符串，整数)
- set   
    1.元素不重复的集合
    2.可以理解为set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。所以都是大括号{}
    3.add,remove

'''

dic={'Colin':'Briliant','Bob':20,1:'A'}
print(dic['Colin'])
print(dic['Bob'])
print(dic[1])
dic['Adam']=99
print(dic)

#安全判断
if 'Bob' in dic:
    print('True')

if 'xx' in dic:
    print('True')
else:
    print('No')

#返回None
print(dic.get('AA'))
#自己指定返回值
print(dic.get('AA',-1))

dic.pop('Bob')
print(dic)




s=set([1,1,2,3])
print(s)

s1=set([1,2,3])
s2=set([2,3,4])
#取交集
print(s1&s2)
#取并集
print(s1|s2)

#再议不可变对象
a='abc'
#创建了新的字符串赋值给b
b=a.replace('a','A')
print(a)
print(b)


