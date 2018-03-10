'''
1、 Counter 本身用来计数用的

2、 使用Counter需要提前导入collections模块： import collections

3、 常用函数
    Counter()           本身用来给传入的字符串或者列表等参数计数用。生成类似字典的显示格式
    most_common()       显示重复次数最多的前几个元素
    elements()          显示原来的所有元素（可用items() keys() values() 函数显示指定内容）

4、 自定义的可用来测试的函数
    My_Counter()
    My_most_common()
    My_elements()
'''





#导入collections模块
import collections


def My_Counter():
    obj = collections.Counter('aabbccddef')
    print(obj)
    #Counter({'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 1, 'f': 1})
#My_Counter()




def My_most_common():
    obj = collections.Counter('aaaaaabdbbbccddddddef')
    print(obj)
    ret = obj.most_common(3)
    print(ret)                      #显示重复次数最多的前三个
#My_most_common()




def My_elements():
    obj = collections.Counter('aaaaabbccccccccdddddd')

    for a in obj.elements():
        print(a)                    #获取所有元素（元素有多少个就出现多少次）

    for k in obj.keys():
        print(k)                     #获取所有单个元素

    for v in obj.values():
        print(v)                      #获取所有value，即元素出现次数

    for k,v in obj.items():
        print(k,v)                   #获取所有key和values(元素出现次数)
#My_elements()




obj = collections.Counter('aaaaabbccccccccdddddd')
print(obj)
