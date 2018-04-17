'''装饰器详解'''
'''
装饰器：
定义：本质是函数，（装饰其他函数）就是为其他函数添加附加功能
原则：	1、不能修改被装饰的函数的源代码
		2、不能修改被装饰的函数的调用方式



实现装饰器知识储备：
	1、函数即"变量"
	2、高阶函数
		a：把一个函数名当做实参传给另外一个函数（在不修改被装饰函数源代码的情况下为其添加功能）
		b：返回值中包含函数名（不修改函数的调用方式）
	3、嵌套函数

	高阶函数+嵌套函数 =》装饰器
'''




def b1():
    #符合a第一个标准的高阶函数(把一个函数名当做实参传给另外一个函数)

    def bar():
        print('in the bar')

    def test1(func):
        print(func)
        func()

    test1(bar)

# b1()







def b2():
    # 按照符合a第一个标准的高阶函数--写的代码的作用示例（可以使用test1函数为bar函数加一个记录代码运行时间的功能，此时test1相当于一个装饰器）


    import time

    def bar():
        time.sleep(3)
        print('in the bar')

    def test1(func):
        start_time=time.time()			#记录当前时间给start_time
        func()
        stop_time=time.time()			#记录当前时间给stop_time
        print("the func run time is %s" %(stop_time-start_time))		#打印func的运行时间等于结束时间减去开始时间

    test1(bar)

# b2()









def b3():
    # 符合b第二个标准的高阶函数(返回值中包含函数名)


    import time

    def bar():
        time.sleep(3)
        print('in the bar')

    def test2(func):
        print(func)
        return func

    print(test2(bar))			#test2(bat)函数执行本身会打印bar函数的内存地址，return返回值也是bar函数的内存地址，掐面加上print也会打印出来

#b3()









def b4():
    import time

    def bar():
        time.sleep(3)
        print('in the bar')

    def test2(func):
        print(func)
        return func

    t=test2(bar)

b4()







def b5():
    import time

    def bar():
        time.sleep(3)
        print('in the bar')

    def test2(func):
        print(func)
        return func

    t=test2(bar)
    t()

# b5()




def b6():
    # 示例四（不修改函数的调用方式:bar() 的情况下，给bar函数新增功能print(func)）

    import time

    def bar():
        time.sleep(3)
        print('in the bar')

    def test2(func):
        print(func)
        return func

    bar=test2(bar)			#先执行了test2(bar)，然后把return结果重新赋值给了新的bar，下面再执行了新bar
    bar()

#b6()




