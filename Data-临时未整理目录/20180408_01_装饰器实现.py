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
#tv("zhangcy")

