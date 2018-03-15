'''
1、 对于[数字]和[字符串]而言，赋值、浅拷贝和深拷贝无意义，因为其永远指向同一个内存地址
2、 对于字典、元祖、列表而言，进行赋值、浅拷贝和深拷贝时，其内存地址的变化是不同的。


赋值： 只是创建一个变量，该变量指向原来内存地址
浅拷贝：在内存中只额外创建第一层数据
深拷贝：在内存中将所有的数据重新创建一份（排除最后一层，即：python内部对字符串和数字的优化）


'''

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







def ZCY_Copy():
    A = {'K1':'V1','K2':'V2','K3':[11,22,33]}
    B = copy.copy(A)
    C = copy.deepcopy(A)

    print('为原始数据字典A的ID= ',id(A))
    print('使用浅拷贝字典B的ID= ',id(B))
    print('使用深拷贝字典C的ID= ',id(C))

    print()
    print('字典A的K3的ID= ',id(A['K3']))
    print('字典B的K3的ID= ',id(B['K3']))
    print('字典C的K3的ID= ', id(C['K3']))

    print()
    print('可以看出使用浅拷贝复制的字典B和原始字典A的K3的ID是一样的，所以如果修改了字典B的K3的元素，等于修改了ID一样的A的K3对应的元素；；所以如果有多层数据拷贝的需求，要使用深拷贝copy.deepcopy()')

    print()
    print('字典A的K1的ID= ',id(A['K1']))
    print('字典C的K1的ID= ',id(C['K1']))
    C.
ZCY_Copy()

