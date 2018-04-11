import time
def XF(name):
    print("选手 [%s] 就位！" % name)
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



'''
1、导入import模块
2、把XF函数载入到内存中
3、把ZZ函数载入到内存中
4、执行ZZ函数
    5、首先定义 c 等于函数XF('A')的执行结果
        c的内容就为：
            print("%s 准备吃包子了" % name)
            while循环的内容
            
    
    6、执行c.__next__()，首先打印我要准备吃包子了
        但是向下执行的时候，while循环遇到了yield，并且yield没有内容，所以XF函数不会向下执行，ZZ函数向下运行
    7、打印我要准备吃包子
    8、等了一秒
    9、打印做了两个包子
    10、给c发送了一个参数，给到了baozhi
        print("包子[%s]来了，被[%s]吃了！ " %(baozi,name))
    11、给了c10次，打印10次
'''
