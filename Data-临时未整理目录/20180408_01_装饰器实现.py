'''
def login(func):
    print("验证身份")
    return func

def tv(name):
    print("欢迎 [%s] 来到TV页面" %name)

tv = login(tv)
tv("zhangcy")
'''


#下面代码效果等同于上面代码，不过上面代码等于对函数做了替换tv = login(tv)（还是修改了原来的结构），而下面的代码纯粹只是扩展了功能。



def login(func):                                                    #func = tv
    def inner(arg):
        print("验证身份")
        func(arg)                                                   #tv
    return inner

@login
def tv(name):
    print("欢迎 [%s] 来到TV页面" %name)

#tv = login(tv)
tv("zhangcy")



'''理解
1、先把login函数加载到内存中
2、@login相当于把tv函数作为login函数的参数来运行一遍login函数（相当于执行tv = login(tv)）。
    3、login函数里面，此时tv函数就赋值给了func参数，把inner函数加载到内存中，然后return返回inner函数的内存地址(执行结束login函数这时tv就指向了inner函数的内存地址)
4、运行函数tv("zhangcy"),相当于执行了：
     def inner(arg):            其中inner被tv替换，arg被zhangcy替换
        print("验证身份")
        func(arg)                func等于之前的tv函数，并且给其复制arg（值为zhangcy）
    

'''

