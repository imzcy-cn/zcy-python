#一个参数
print('一个参数')
def show(zcy):
    print(zcy)
show('zhangcy')

print()




#两个参数（如果定义两个参数，但是使用的时候只给了一个参数会报错）
print('两个参数')
def show2(aa,bb):
    print(aa,bb)
show2('zhangcy','ok')

print()



#默认参数(默认参数必须要写在最后面)
#如果给bb赋值则使用给定的888，如果bb不给值，则应用默认的999
print('默认参数')
def show3(aa,bb=999):
    print(aa,bb)
show3(111)
show3(111,888)

print()




#指定参数
print('指定参数')
def show4(aa,bb):
    print(aa,bb)
show4(bb=999,aa=111)

