


'''元祖
#定义一个元祖
    a = (1,2,3)             用()包裹的元素成为元祖，等同于a = tuple(1,2,3)

元祖的值是只读的，用dir()方法可以看出元祖dir(a)，所能操作的方法只有count和index
'''




'''查看元祖所支持的方法
>> > a = (1, 2, 3, 4, 5, 6)
>> > dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__',
 '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__',
 '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>> >

'''


type() 方法可以获取类型，直接变量赋值修改变量的类型



'''列表转换为元祖

    >> > b = ['a', 'b', 'c', 'd']
    >> > type(b)
    < class 'list'>
    
    >> > a = tuple(b)
    >> > a
    ('a', 'b', 'c', 'd')
    >> > type(a)
    < class 'tuple'>
'''




'''元祖转换为列表

    >> > a
    ('a', 'b', 'c', 'd')
    >> > type(a)
    < class 'tuple'>
    
    >> > b = list(a)
    >> > b
    ['a', 'b', 'c', 'd']
    >> > type(b)
    < class 'list'>
    >> >
'''