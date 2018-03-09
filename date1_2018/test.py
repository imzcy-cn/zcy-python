import sys

ChuShi = 0
JieShu = 3

username = input("Please input your username: ")


while ChuShi < JieShu:
    with open('LockFile.txt','r') as LockFile:
        for line in LockFile.readlines():
            if len(line.strip()) == 0:
                continue
            if line.strip() == username:
                print('您的账号已被锁定！')
                sys.exit(0)
                #sys.exit('您的用户已被锁定！')

        if len(username) == 0:
            print('用户名不能为空，请重新输入！')
            continue

'''
        pwd = input("Please your password: ")
        with open('myuser.txt','r') as UserFile:
            for line in UserFile.readlines():
                u = line.strip()
                u = u.split()
                if username == u[0] and pwd == u[1]
                    print('登录成功')
                    break
'''









