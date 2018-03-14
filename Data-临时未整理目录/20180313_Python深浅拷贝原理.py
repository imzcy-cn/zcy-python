'''
对于 数字 和 字符串 而言，赋值、浅拷贝和深拷贝无意义，因为其永远指向同一内存地址。
对于字典、元祖、列表而言，进行赋值、浅拷贝和深拷贝时，其内存地址的变化是不同的。
赋值，只是创建一个变量，该变量指向原来内存地址。



#浅拷贝
copy.copy()

#深拷贝
copy.deepcopy()

#赋值
 =
'''




import copy

'''
#对于 数字 和 字符串 而言，赋值、浅拷贝和深拷贝无意义，因为其永远指向同一内存地址
a1 = "zhangcy"
print('a1= ',id(a1))

a2 = a1
print('a2= ',id(a2))

a3 = copy.copy(a1)
print('a3= ',id(a3))

a4 = copy.deepcopy(a1)
print('a4= ',id(a4))
'''





n1 = {'k1':'wu','k2':'123','k3':['zcy',456]}
print('n1= ',id(n1))

n2 = n1
print('n2= ',id(n2))

n3 = copy.copy(n1)                              #n3 为浅拷贝
print('n3= ',id(n3))

n4 = copy.deepcopy(n1)                          #n4为深拷贝
print('n4= ',id(n4))



print('k3 as n3= ',id(n3['k3']))
print(n3['k3'])
print('k3 as n1= ',id(n1['k3']))
print(n1['k3'])
print()


print('k3 as n4= ',id(n4['k3']))
print(n4['k3'])
print('k3 as n1= ',id(n1['k3']))
print(n1['k3'])
