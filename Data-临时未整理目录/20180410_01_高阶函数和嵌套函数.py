#一、函数即变量

def a1():
    #定义了一个简单的函数(相当于定义了一个变量，test1 = time.sleep(3) \n print('in the test1'))
    import time

    def test1():
        time.sleep(3)
        print('in the test1')

    test1()
#a1()





def a2():
    #定义了一个嵌套函数

    def foo():
        print('in the foo')
        bar()

    def bar():
        print('in the bar')

    foo()

# a2()






def a3():
    #定义了一个高阶函数（）
    import time

    def bar():
        time.sleep(3)
        print('in the bar')

    def test2(func):
        print(func)
        return func

    print(test2(bar))

a3()








def a4():
    import time

    def bar():
        time.sleep(3)
        print('in the bar')

    def test2(func):
        print(func)
        return func

    t = test2(bar)
    t()

#a4()








def a5():
    import time

    def bar():
        time.sleep(3)
        print('in the bar')

    def test2(func):
        print(func)
        return func

    bar = test2(bar)
    bar()

#a5()










######################################################################################################################
#函数嵌套示例详解
'''
在函数内部定义的函数，可以理解为局部变量，只能在外层的函数内调用
'''



def a6():
    def foo():
        #定义了一个嵌套函数bar()，bar函数只能在foo()函数内被调用

    	print('in the foo')
    	def bar():
    		print('in the bar')
    	bar()

    foo()

#a6()





def a7():
    #嵌套函数的应用顺序

    x=0
    def a():
        x=1
        def b():
            x=2
            def c():
                x=3
                print(x)
            c()
        b()
    a()
#最终返回结果是3
#如果定义好函数b后下面没有执行b()函数或则c()函数，则没有返回值，

# a7()























#######################################################################################################################
'''三、装饰器的实现： 高阶函数+嵌套函数'''
#######################################################################################################################




def a8():
    #装饰器的实现

    import time
    def bar():
        time.sleep(3)
        print('in the bar')

    def zcy(func):
        def zs():
            start_time=time.time()
            func()
            stop_time=time.time()
            print("the bar run time is [%s] 秒" %(stop_time-start_time))
        return zs

    bar=zcy(bar)
    bar()

#其实就是新定义了一个函数zs()，把bar函数现有代码和新增功能代码整合到一起又重新赋值给了bar，，bar = bar + 附加功能

#装饰器其实就是定义一个函数bar = bar + 附加功能
# a8()








def a9():
    import time

    def zcy(func):
        def zs():
            start_time = time.time()
            func()
            stop_time = time.time()
            print("the bar run time is: %s" % (stop_time - start_time))
        return zs

    # 解释下：@符号后面跟函数，就是装饰器，@zcy 就相当于执行 bar=zcy(bar)
    @zcy
    def bar():
        time.sleep(3)
        print('in the bar')

    bar()

# a9()

