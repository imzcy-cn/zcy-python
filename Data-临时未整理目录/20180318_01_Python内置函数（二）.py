'''
eval()
map()               遍历序列，对序列中每个元素进行操作，最终获取新的序列。
filter()            对于序列中的元素进行筛选，最终获取符合条件的序列
float()             把对象转换为浮点数类型
format()            使用动态参数实现字符串格式化
frozenset()         不能增加修改的集合
getattr()
globals()           当前所有可用的变量
hasattr()
hash()
help()
hex()               转换为十六进制(0x)
id()
input()
int()
isinstance()
issubclass()
iter()
len()
list()
locals()
map()
max()               最大值
min()               最小值
memoryview()
next()
object()
oct()               八进制
open()
ord()
pow()
print()
range()             拿到一个区间
repr()              返回一个字符串(让机器调用的)
reversed()          反转
round()             四舍五入
set()
setattr()
slice()
sorted()            排序
staticmethod()
str()
sum()               求和
super()             执行父类
tuple()
type()
vars()              vars把所有的key和values都显示出来了
dir()               显示所有的key
zip()



'''



'''自定义函数演示系统函数示例：
ZCY_Filter()
ZCY_Format()

'''





'''eval()               #引号包裹的字符串6*8，能根据连接符做算术运算。（+，-，*，/）
>>> "6*8"   
'6*8'
>>> eval("6*8")
48
>>>
'''



''' map()       #map有两个参数，第一个为函数，后面为循环执行的对象。处理每个元素加入到一个新列表
>>> li = [11,22,33,44]
>>> new_li = map(lambda x:x+100,li)
>>> new_li = list(new_li)
>>> print(new_li)
[111, 122, 133, 144]
>>>

#第二种写法：直接写好函数
li = [11,22,33,44]
def zcy(x):
    return x+100

new_li = map(zcy,li)
list(new_li)


'''




''' filter()     #过滤
li = [11,22,33,44]
def zcy(x):
    if x>33:
        return True
    else:
        return False

new_li = filter(zcy,li)
list(new_li)                    #只显示44


'''





''' filter() 函数示例：
>>> def zcy(x):
...     if x>33:
...         return True
...     else:
...         return False
...
>>>
>>>
>>> li = [11,22,33,44]
>>> new_li = filter(zcy,li)
>>> li
[11, 22, 33, 44]
>>> list(new_li)
[44]
>>>

'''




def ZCY_Filter():
    def zcy(x):
        if x>33:
            return True
        else:
            return False
    li = [11,22,33,44]
    new_li = filter(zcy,li)
    print(li)
    print(list(new_li))

#ZCY_Filter()


def ZCY_Format():
    t = "{0} is {1}"
    S = ['ZCY','OK']
    bb = t.format(*S)
    print(bb)
#ZCY_Format()




def ZCY_Zip():
    z = [1,2,3]
    c = [4,5,6]
    y = zip(z,c)
    print(list(y))



