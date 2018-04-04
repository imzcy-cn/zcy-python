import time
def chi(name):
    print("[%s] 就位！" %name)
    while True:
        baozhi = yield
        print("包子 [%s] 来了，被 [%s] 吃掉了！" %(baozhi,name))


def zz():
    C = chi("A")                                #定义C 等于上面变量chi()，并给一个参数A
    C.__next__()                                #获取C的迭代器的值
    print("我要开始准备吃包子了")
    for  i in range(10):
        time.sleep(1)
        print("做了两个包子")
        C.send(i)
zz()
