'''创建SET对象
s1 = set()

1、访问速度快
2、天生解决重复问题

'''

'''Set 常用函数
1、add()                     添加
2、clear()                   清空set内所有数据
3、difference()              找到不同，并把不同的内容放入一个新set里
4、difference_update()       直接修改原有
5、


'''


'''可用作测试的自定义函数
1. set_add()
2. set_difference()
3. set_difference2()
4. 

'''

def set_add():
    s1 = set()
    print('1. ',s1)
    s1.add('zcy')
    print('2. ',s1)
    s1.add('zcy')
    print('3. ',s1)
    s1.add('zhangcy')
    print('4. ',s1)
    print("可以发现第三次添加的同样的内容zcy的时候，set会自动去重，只显示一个")
#set_add()




def set_difference():
    s1 = set(['zhangsan','lisi','wangwu'])
    print('1. ',s1)
    s1.difference(['zhangsan','wangwu'])
    print('2. ',s1)
    s2 = s1.difference(['zhangsan','wangwu','zhangcy'])
    print('3. ',s2)
    print()
    print('''可以发现直接把s1应用函数difference的时候打印机的还是原来的内容，没有任何改变（如第2条打印）。把s1应用函数difference后的内容赋值给s2之后才能有所改变（如第3条打印）"
          s1.difference(['zhangsan','lisi']) ，，就是把s1和diff参数做比较，比较出s1中有哪些内容是diff参数所没有的
          ''')
#set_difference()

def set_difference2():
    s1 = set(['zhangsan','lisi','wangwu'])
    print('s1= ',s1)
    s2 = set(['wangwu'])
    print('s2= ',s2)
    s3 = s1.difference(s2)
    print('s3= ',s3)
    print()
    print("s3等于s1.difference(s2) 即比较S1中有哪些内容是S2中没有的赋值给S3  （说明：即使S2有很多S1中没有的数据，但是比较的时候只是比较相对于S1中数据，S2是哪些没有的）")
#set_difference2()




def set_difference_update():
    s1 = set(['zhangsan', 'lisi', 'wangwu'])
    print('1. ',s1)
    s1.difference_update(['zhangsan'])
    print('2. ',s1)
    s2 = s1.difference_update(['zhangsan'])
    print('3. ',s2)

#set_difference_update()


def set_difference_update2():
    s1 = set(['zhangsan','lisi','wangwu'])
    s2 = set(['zhangsan'])
    print('s1= ',s1)
    print('s2= ',s2)

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    s1.difference_update(s2)
    print('s1.difference_update(s2)               =     ',s1)
    s3 = s1.difference_update(s2)
    print('s3 = s1.difference_update(s2) , s3     =     ',s3)

    print()
    print("可以发现difference_update()函数不会生成引得set，直接修改原来的set"
          "S1.difference(S2) 就是把S1中包含的S2有的数据都删除掉")
set_difference_update2()

