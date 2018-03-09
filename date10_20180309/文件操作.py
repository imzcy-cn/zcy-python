
'''
2.7 版本Python操作文件
    file_obj = file("文件路径","模式")

3.0 版本Python操作文件
    file_obj = open("文件路径","模式")


模式：
    r       只读
    w       覆盖写入（如果文件不存在则创建）
    a       追加写入
    w +     覆盖读写（文件不存在则创建）

'''





'''
读取文件内容：
# 一次性加载所有内容到内存
obj.read()

# 一次性加载所有内容到内存，并根据行分割成字符串
obj.readlines()

# 每次仅读取一行数据
for line in obj:
    print
    line


写文件的内容：
obj.write('内容')

关闭文件句柄：
obj.close()


with open(locked_file, 'r') as lock_f:           打开锁文件，赋值给变量lock_f

import time

time.sleep(1)  # 暂停一秒


strip()     方法去除对象两边空格和回车
split()     方法把对象按空格分隔为列表

'''






# ++++++++++++++++++++++++++++操作文件++++++++++++++++++++++++++++#
'''只读
MyFile = 'E:\zcy-python\ZCY-LaoNanHaiPythonZiDongHua12\myuser.txt'
zcy = open(MyFile,'r')

for line in zcy:
    print(line)
zcy.close()
'''


'''覆盖写入

zcy = open('user.log','w')

zcy.write('this is the first line\n')
zcy.write('this is the second line\n')
zcy.write('this is the 3 line\n')

zcy.close()
'''


'''追加写入

zcy = open('user.log','a')

zcy.write('this is the 5 line\n')

zcy.close()
'''


'''只读（按行打印user.log文件内容）
zcy = open('user.log','r')

for line in zcy:
    print(line.strip())                 #strip()用来去除打印换行符，，2.0版本的Python直接print line, 就好（line后面加一个,号）

zcy.close()
'''


'''判断user.log文件中某一行是否为this is the 5 line

zcy = open('user.log','r')

for line in zcy:
    #if '6' in line:
    if 'this is the 5 line' == line.strip():
        print('5555555')
    else:
        pass

zcy.close()
'''

'''
# 读的模式不能写入，写的模式下读也会报错




'''
zcy = open('user.log','w+')

zcy.write('new line\n')
print("123",zcy.readlines())

zcy.close()
'''

zcy = open('myuser.txt', 'r')

print(zcy.readlines())

zcy.close()




