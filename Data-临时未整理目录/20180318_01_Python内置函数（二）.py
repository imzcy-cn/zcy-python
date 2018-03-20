'''
eval()
map()              遍历序列，对序列中每个元素进行操作，最终获取新的序列。
filter()           对于序列中的元素进行筛选，最终获取符合条件的序列

'''



'''自定义函数演示系统函数示例：
ZCY_Filter()


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



t = "{0} is {1}"
format()
