import time
def XF(name):
    print("%s 准备吃包子了" % name)
    while True:
        baozi = yield
        print("包子[%s]来了，被[%s]吃了！ " %(baozi,name))


def ZZ():
    c = XF('A')
    #c2 = XF('B')
    c.__next__()
    #c2.__next__()
    print("我要准备吃包子了")
    for i in range(10):
        time.sleep(1)
        print("做了两个包子")
        c.send(i)
        #c2.send(i)
ZZ()

