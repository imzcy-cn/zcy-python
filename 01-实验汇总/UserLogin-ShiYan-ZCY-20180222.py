'''
1、本实验有三个文件
    1. UserLogin.py     主执行程序
    2. UserFile.txt     存放登录用户名密码文件（每行以空格分开用户名和密码）
    3. LockFile.txt     存放锁定用户名文件（每行一个用户名）

2、实验内容
    1. 模拟用户登录，获取用户输入的用户名和密码
    2. 如果用户输入的用户名不存在(不在UserFile.txt里面)，提示输入用户名不存在，输入错误3次退出程序。
    2. 如果用户输入的用户名存在，并且在LockFile.txt锁文件里面，则提示用户名已被锁定，直接退出。
    3. 如果用户输入用户名存在，则提示输入密码，
    4. 用户名密码输错3次锁定该用户（把用户名追加到锁文件LockFile.txt里面）


3、
'''



import sys
ChuShi = 0
JieShu = 3


username = input('Please input your name: ')
with open('LockFile.txt','r') as LockFile:
    for line in LockFile.readlines():
        if len(line.strip()) == 0:
            continue
        if line.strip() == username:
            print('您的账号已被锁定！')
            sys.exit(1)

while ChuShi < JieShu:
    ChuShi+=1
    pwd = input('Please input your password: ')
    with open('UserFile.txt','r') as UserFile:
        for line in UserFile.readlines():
            u = line.strip()
            u = u.split()

            if u[0] == username and u[1] == pwd:
                print('登录成功')
                sys.exit(0)
print('错误次数太多,账号已被锁定')
with open('LockFile.txt','a') as suo:
    suo.write(username)
    suo.write('\n')
    sys.exit(1)
