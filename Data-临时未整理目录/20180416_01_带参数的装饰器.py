''''''
#######################################################################################################################
def a1():

    #不带参数的装饰器

    def zcy(func):
        def zs():
            start_time = time.time()
            func()
            stop_time = time.time()
            print("the bar run time is: %s" % (stop_time - start_time))

        return zs

    @zcy
    def test1():
        time.sleep(2)
        print('in the bar')

    test1()






#######################################################################################################################




def a2():
    # 带一个参数的装饰器

    import time

    def zcy(func):
        def zs(arg):
            start_time = time.time()
            func(arg)
            stop_time = time.time()
            print("the bar run time is: %s" % (stop_time - start_time))

        return zs

    @zcy
    def test2(name):
        print("test2: ", name)

    test2('zhangcy')








#######################################################################################################################
def a3():
    # 带两个参数的装饰器

    import time

    def zcy(func):
        def zs(arg, arg2):
            start_time = time.time()
            func(arg, arg2)
            stop_time = time.time()
            print("the bar run time is: %s" % (stop_time - start_time))

        return zs

    @zcy
    def test2(name, age):
        print("test2: ", name, age)

    test2('zhangcy', '18')














#######################################################################################################################
#按照上面的代码定义一个装饰器，如果只有一个函数应用装饰器或则如果都是同一类型的都带固定参数还好，如果有多个函数都要应用该装饰器，并且有的
#函数不需要参数，有的函数要输入一个参数，有的函数需要多个参数，此时装饰器就会报错(如下所示)。


'''
import time

def zcy(func):
    def zs(arg,arg2):
        start_time = time.time()
        func(arg,arg2)
        stop_time = time.time()
        print("the bar run time is: %s" % (stop_time - start_time))
    return zs

@zcy
def test1():
    time.sleep(2)
    print('in the bar')


@zcy
def test2(name,age):
    print("test2: ",name,age)

test1()
test2('zhangcy','18')
'''




#解决方式详看下节内容《20180416_02_带任意个数参数的装饰器.py》
