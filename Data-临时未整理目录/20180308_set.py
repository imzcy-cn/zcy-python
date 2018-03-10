'''SET的常用方法
S1 = set()

S1.difference()                             #生成新对象
S1.difference_update()                      #直接操作原数据
S1.isdisjoint()                             #如果没有父集，返回True
S1.issubset()                               #是否是子集
S1.issuperset()                             #是否是父集
S1.pop()                                    #删除（从集合里面拿到一个数据，并且可以用=赋值给一个变量。并移除原来集合中该数据）
S1.remove()                                  #只删除集合中数据，不能赋值（赋值后结果为None）并且remove必须指定参数（要删除哪个内容）
S1.union()                                  #并集
S1.update()                                 #取更新
S1.symmetric_difference(S2)                 #获取S1和S2所有不相同的元素（直接S3 = S1.symmetric_difference(S2)）
                                            #相当于S1.difference(S2) + S2.difference(S1)

'''


def set_difference():
    S1 = set(['A','B','C'])
    S2 = set(['B','D'])
    S1.difference(S2)
    print(S1)                       #直接对S1使用difference函数后S1本身内容没有发生任何变化，而把执行结果赋值给S3后则有变化；（说明difference函数是生成新函数）

    S3 = S1.difference(S2)
    print(S3)
#set_difference()



def set_difference_update():
    S1 = set(['A', 'B', 'C'])
    S2 = set(['B','D'])
    S1.difference_update(S2)
    print('S1= ',S1)            #直接对S1使用difference_update函数，S1内容为删除S2包含S1的内容之后内容（直接修改原数据）

    S3 = S1.difference_update(S2)
    print('S3= ',S3)

#set_difference_update()


def set_isdisjoint():
    print(123)


def set_pop():
    S1 = set(['A', 'B', 'C'])
    print(S1)
    S2 = S1.pop()
    print(S1)
    print(S2)                           #可以把pop删掉的值赋值给一个变量

#set_pop()


def set_remove():
    S1 = set(['A', 'B', 'C'])
    #1.测试一
    S1.remove('B')                      #remove必须制定要删除的内容
    print(S1)

    #2.测试二
    #S2 = S1.remove('B')                 #remove函数不能赋值，复制后打印出来None(没有返回值)
    #print(S2)

#set_remove()



#旧数据
S1 = set(['#1','#2','#3'])

#新数据
S2 = set(['#1','#3','#4'])

#要更新数据          都有的需要更新
#要删除数据          旧的有，新的没有，需要删除
#要新增数据          新的有，就得没有

D = S1.difference(S2)                   #去掉S2包含在的S1内的那些需要更新的数据  剩下的就是需要删除的
U = S1.difference(D)                    #S1中去掉需要删除的，就是需要更新的
I = S2.difference(U)                    #S2中去掉需要更新的，就是需要新增的
                                        #可以画两个重叠部分区域的圆圈来帮组思考

print('需要删除的数据： ',D)
print('需要更新的数据： ',U)
print('需要新增的数据： ',I)







#S1.difference(S2)       相当于循环S2里面的元素，如果元素in S1，那么删除S1中对应的元素。最后把S1剩下的元素赋值给一个新的变量

