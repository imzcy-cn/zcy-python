def login(func):
    def inner(arg):
        print("验证身份")
        func(arg)
    return inner


def tv(name):
    print("欢迎 [%s] 来到TV页面" %name)

tv = login(tv)
tv("zhangcy")







#上面代码等同于下面

'''

def login(func):
    def inner(arg):
        print("验证身份")
        func(arg)
    return inner

@login
def tv(name):
    print("欢迎 [%s] 来到TV页面" %name)

tv("zhangcy")

'''

#1、先把login(func)函数载入内存中
#2、@login执行tv = login(tv)
    #3、执行login(func)函数，此时func等于tv的内存地址
    #4、定义函数inner(arg)，返回inner函数的内存地址给到tv函数
#5、执行tv("zhangcy")函数，相当于执行
         '''def inner(arg):     
        print("验证身份")
        func(arg)
        '''
         #此时arg等于"zhangcy"，接着打印验证身份，接着执行函数func(arg)，func为之前的tv，arg为zhangcy
         # def tv(name):
         #print("欢迎 [%s] 来到TV页面" %name)


