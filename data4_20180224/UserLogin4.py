import sys
ChuShi = 0
JieShu = 3


while ChuShi < JieShu:

    username = input('Please input your name: ')

    with open('LockFile.txt','r') as LockFile:
        for line in LockFile.readlines():
            if line.strip() == username:
                print('您的账号已被锁定！')
                sys.exit(1)

            with open('UserFile.txt', 'r') as UserFile:
                a = False
                for zcy in UserFile.readlines():
                    u = zcy.strip()
                    u = u.split()
                    if username == u[0]:
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



                    if ChuShi == 2:
                        print("错误次数太多")
                        sys.exit(1)
        if a == True:
            continue
        print('您输入账号不存在，请重新输入！')
        ChuShi+=1