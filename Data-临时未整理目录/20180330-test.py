'''
def power(x,y):
    s = x ** y
    return s
'''


def zcy(a):
    while a > 0:
        a -= 1
        yield 1
        print("哈哈哈哈")
atm = zcy(5)
#print(type(atm))            #一个函数调用时返回一个迭代器，那这个函数就叫做生成器（generator），如果函数中包含yield语法，那这个函数就会变成生成器


print(atm.__next__())
print(atm.__next__())





