'''
eval()
filter()
map()

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





