'''
defaultdict是对字典类型的补充，它默认给字典的值设置了一个类型

__contains__ 方法用来判断一个key是否存在，如果存在返回True，如果不存在返回False

'''

#首先导入collections模块
import collections

def ZCY_DefDict():
    values = [1,3,5,7,9,2,4,6]
    dic = {}

    for value in values:
        if value > 5:
            if dic.__contains__('k1'):                              #如果存在k1这个键，则append添加；否则定义一个k1值为value
                dic['k1'].append(value)
            else:
                dic['k1'] = [value]
        else:
            if dic.__contains__('k2'):
                dic['k2'].append(value)
            else:
                dic['k2'] = [value]
    print(dic.items())



#上面代码可以使用defaultdict()方法精简为以下代码
'''
values = [1,3,5,7,9,2,4,6]
dic = collections.defaultdict(list)
for value in values:
    if value > 5:
        dic[k1].append(value)
    else:
        dic['k2'].append(value)
'''







def ZCY_Dict_None():
    dic = {'k1':None}                       #给key设置一个空的时候，是不能使用append添加的
    dic['k1'].append('zhang')
    print(dic)


def ZCY_Dict_List():
    dic2 = {'k1':[]}                        #给key的value设置为一个空的列表，是可以应用append()方法添加value的
    dic2['k1'].append('zhang')
    print(dic2)




def ZCY_DefaultDict():                              #defaultdict()方法的用途
    dic =  collections.defaultdict(list)
    dic['k1'].append('zhang')
    print(dic)
#ZCY_DefaultDict()


