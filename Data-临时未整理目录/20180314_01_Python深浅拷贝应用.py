

#首先导入copy模块
import copy



def ZCY_FuZhi():
    a = [1,2,3,4]
    b = a
    print('id as a= ',id(a))
    print('id as b= ',id(b))

    print('a= ',a)
    print('b= ',b)

    print("为b追加5")
    b.append(5)                             #因为a和b指向的是同一id对应的值，所以修改b对应内存空间id对应的值得时候，查看a也会随之改变

    print('id as a= ',id(a))
    print('id as b= ',id(b))

    print('a= ',a)
    print('b= ',b)





print('Dic= ',dic)
print('id as Dic=     ',id(dic))

print()

#NewDic = dic
#print('NewDic= ',NewDic)
#print('id as NewDic= ',id(NewDic))

print()
print()

'''
NewDic = copy.copy(dic)
print('NewDic_copy.cpy= ',NewDic)
print('id as NewDic= ',id(NewDic))

NewDic['CPU'] = 50

print(dic)
print(NewDic)
'''

'''
NewDic = copy.deepcopy(dic)
print('NewDic_copy.deepcopy= ',NewDic)
print('id as NewDic= ',NewDic)

print()

NewDic['CPU'][0] = 50
print(NewDic)
print(dic)
'''



dic = {
    "CPU":[80,],
    "Mem":[80,],
    "Disk":[80,]
}

