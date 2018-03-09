import sys
ChuShi = 0
JieShu = 3

'''
def mima(u):
    pwd = input('Please input your password: ')
    if u[0] == u[1]:
        print('登录成功！')
    else:
        print("密码错误，请重新输入")
        ChuShi+=1
'''



while ChuShi < JieShu:

    username = input('Please input your name: ')            #获取用户名

    with open('LockFile.txt','r') as LockFile:
        for line in LockFile.readlines():
            if line.strip() == username:                        #如果用户名存在锁文件里面，则打印已锁定，然后退出
                print('您的账号已被锁定！')
                sys.exit(1)

            with open('UserFile.txt', 'r') as UserFile:
                a = False
                for zcy in UserFile.readlines():
                    u = zcy.strip()
                    u = u.split()
                    print('u0='+u[0])
                    if username == u[0]:                            #否则如果输入用户名等于存在的用户名，则跳过
                        pwd = input('Please input your password: ')
                        print('u0='+u[0])
                        print('u1='+u[1])
                        if u[0] == username and u[1] == pwd:
                            print('登录成功！')
                            exit(0)
                        else:
                            print("密码错误，请重新输入")
                            ChuShi += 1
                            a = True
                            break



                    if ChuShi == 3:
                        print("错误次数太多")
                        sys.exit(1)
        if a == True:
            continue
        print('您输入账号不存在，请重新输入！')
        ChuShi+=1
        print('跳过一次循环')

