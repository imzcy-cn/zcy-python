'''
return 可以做返回值
return 遇到return之后，函数的内容就终结了，不会往下执行了（类似于循环中break和continue）
'''


def show2():
    print('a')
    if 1 == 1:
        return [11,22]          #如果1==1，那么return指定返回值之后，代码就结束了，不会向下继续执行。
    print('b')

ret = show2()
print(ret)


