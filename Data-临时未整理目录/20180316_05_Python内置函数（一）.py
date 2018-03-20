'''

内置函数:

    abs()            绝对值
    all()            所有的元素都是真的情况下，返回真；None是假的，空字符串是假的bool("")，空列表是假的bool([])，空元祖是假的bool(())，空字典是假的bool({})
    any()            任何，只要里面元素有一个真的，就返回True
    ascii()
    bool()           查看布尔值
    bin()            二进制，0b表示二进制
    bytearray()     把汉字转换为字节数组的
    bytes()
    callable()      判断是否可执行
    chr()           是否可执行（变量后面能加()就是可执行）
    chr()           把数字转换为字符
    ord()           把字符转换为数字
    compile()       编译
    complex()       复数
    delattr()       反设
    dict()
    dir()           当前变量所有key
    divmod()
    enumerate()
'''


'''
    >>> bool(None)
    False
    >>> bool("")
    False
    >>> bool(" ")
    True
    >>> bool([])
    False
    >>> bool(())
    False
    >>> bool({})
    False
    >>>

'''

'''any  任何，只要里面元素有一个真的，就返回True
>>> any(["",[],(),{},None])
False
>>> any(["",[],(),{},None,1])
True
>>>
'''



''' bin()   二进制
>>> bin(10)
'0b1010'
>>>
'''




'''
p = bytearray('张辰',encoding='utf-8')
print(p)
'''

'''
p = bytes('张辰',encoding='utf-8')
print(p)
'''



'''callable 判断是否可执行，能执行返回True
>>> f = lambda x:x+1
>>> f(5)
6
>>> callable(f)
True
>>> l = []
>>> l()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
>>> callable(l)
False
>>>
'''




''' ord()把ASCII字符转换为数字，chr()把数字转换为ASCII字符
>>> ord('Z')
90
>>> chr(90)
'Z'

>>> import random                               #可以用来生成随机验证码。导入random模块使用random.randint(1,99)生成1-99之间的随机整数，然后用chr()方法转换为对应ASCII字符
>>> random.randint(1,99)
47
>>> chr(47)
'/'
>>>

'''





''' enumerate 
>>> z = ['zhangsan','lisi','wangwu']
>>> for i in z:print(i)
...
zhangsan
lisi
wangwu
>>>
>>> for i,item in enumerate(z,1):print(i,item)              #额外加了一个自增的一列。1开始就是123.
...
1 zhangsan
2 lisi
3 wangwu
>>>
'''




