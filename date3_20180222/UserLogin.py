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
