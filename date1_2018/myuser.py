
'''
只读
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




#读的模式不能写入，写的模式下读也会报错




'''
zcy = open('user.log','w+')

zcy.write('new line\n')
print("123",zcy.readlines())

zcy.close()
'''






zcy = open('myuser.txt','r')

print(zcy.readlines())

zcy.close()




