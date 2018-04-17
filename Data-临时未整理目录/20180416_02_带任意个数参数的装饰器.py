import time

def zcy(func):
    def zs(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("the bar run time is: %s" % (stop_time - start_time))
    return zs

@zcy
def test1():
    time.sleep(2)
    print('in the bar')

@zcy
def test2(name):
    print("test2: ",name)


test1()
test2("zhangcy")