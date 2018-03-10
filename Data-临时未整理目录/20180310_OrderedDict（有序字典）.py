
'''

1、orderdDict是对字典类型的补充，它记住了字典元素添加的顺序

2、常用方法
    popitem()               自动删除字典最后添加的一个item
    pop()                   删除指定key的item，并且有返回值可以把value赋值给新的变量
    setdefault()            设置字典key对应value的默认值(可以指定默认值为什么字符，当key对应的value没有被定义而被调用的时候，使用该参数定义的value)
    update()                如果key存在，则更新value；如果key不存在，则新增

3、自定义用来做测试的函数
    ZCY_Dict()
    ZCY_OrderedDict()
    ZCY_OrderedDict_popitem()
    ZCY_OrderedDict_pop()
    ZCY_OrderedDict_setdefault()
    ZCY_OrderdDict_update()


4、 字典默认输出只输出它的keys
'''



#！！！有序字典实现的方法
#  Dict字典是无序的，但是列表是有序的；可以把列表的元素定义为Dict字典的keys，循环显示列表即能拿到有序的字典values
def ZCY_Dict():
    dic = {'z':'zhangsan','l':'lisi','w':'wangwu'}
    li = ['z','l','w']

    for i in li:
        print(dic[i])
#ZCY_OrderedDict()




#首先导入collections模块
import collections


def ZCY_OrderedDict():
    dic = collections.OrderedDict()
    dic['k1'] = 'v1'
    dic['k2'] = 'v2'
    dic['k3'] = 'v3'

    print(dic)
#ZCY_OrderedDict()




def ZCY_OrderedDict_popitem():
    dic = collections.OrderedDict()
    dic['k1'] = 'v1'
    dic['k2'] = 'v2'
    dic['k3'] = 'v3'

    print(dic)
    dic.popitem()                       # popitem()是自己删除最后的一个数据
    print(dic)
#ZCY_OrderedDict_popitem()





def ZCY_OrderedDict_pop():
    dic = collections.OrderedDict()
    dic['k1'] = 'v1'
    dic['k2'] = 'v2'
    dic['k3'] = 'v3'

    # pop用来删除指定key的value
    print(dic)
    dic.pop('k2')
    print(dic)

    # pop有返回值，可以赋值给ret变量
    ret = dic.pop('k1')
    print(dic)
    print(ret)
#ZCY_OrderedDict_pop()






def ZCY_OrderedDict_setdefault():
    dic = collections.OrderedDict()
    dic['k1'] = 'v1'
    dic['k2'] = 'v2'
    dic['k3'] = 'v3'
    dic.setdefault('k4','666')                  #如果不加参数(666，如果k4没有赋值的话，默认为666)的话，dic.setdefault('k4') 等同于 dic['k4'] = None

    print(dic)

    dic['k4'] = 'v4'
    print(dic)
#ZCY_OrderedDict_setdefault()





def ZCY_OrderdDict_update():
    dic = collections.OrderedDict({'k1':'v2','k2':'v2','k3':'v3'})
    print(dic)

    dic.update({'k2':'v2222','k10':'v10'})
    print(dic)
#ZCY_OrderdDict_update()




