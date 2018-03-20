'''
map()              遍历序列，对序列中每个元素进行操作，最终获取新的序列。
filter()           对于序列中的元素进行筛选，最终获取符合条件的序列




'''

'''自定义函数演示系统函数示例：
ZCY_Filter()


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