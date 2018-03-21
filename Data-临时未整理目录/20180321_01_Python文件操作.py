python 2
next()
readinto()
xreadlines()



python 3
close()                 关闭文件
fileno()                文件描述符
flush()                 把文件刷进硬盘
read()                  读取文件
readable()
seek()                  指定当前指针位置
tell()                  查看当前指针位置。。python3中tell读的是字节。。而read读的是字符
truncate()              打开文件的时候使用r+,使用seek指定指针位置之后，truncate函数会删除指针之后所有内容，只保留指针前面的




def ZCY_Write():
    f = open('test.log','w')
    f.write('123123')
    f.close()

def ZCY_Read():
    f = open('test.log','r')           #打开文件的时候，可以指定编码类型f = open('test.log','r',encoding='utf-8')
    ret = f.read(2)                      #取两个字节
    f.close()
    print(ret)

#一个中文是3个字节。。python3中read是读的字符




def ZCY_Tell():
    f = open('test.log','r',encoding='utf-8')
    print(f.tell())
    f.read(2)                                           #read读进来两个字符
    print(f.tell())                                     #tell则算位移按字节
    f.close()




def ZCY_Seek():
    f = open('test.log''r',encoding='utf-8')
    f.tell()                                        #查看当前指针位置
    f.seek(1)                                       #指定当前指针位置（read从什么地方开始读，1表示第一个字节不读，从第二个字节开始）
    ret = f.read()                                  #read默认读全部，可指定读取字符数
    print(ret)



