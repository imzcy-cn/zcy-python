'''
根据nametuple可以创建一个包含tuple所有功能以及其他功能的类型
'''


#首先导入collections模块
import collections

def ZCY_Tuple():
    t1 = (11,22,33,44)
    print(t1[1])

def ZCY_NameTuple():
    MyTupleClass = collections.namedtuple('MyTupleClass',['z','c','y'])             #自定义类，然后创建对象
    obj = MyTupleClass(11,22,33)
    print(obj.z)
    print(obj.c)
    print(obj.y)
ZCY_NameTuple()

'''
_asdict()       返回xyz所对应的11,22,33
_replace()      值替换

'''
