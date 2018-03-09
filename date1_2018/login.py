'''
locked.txt
zhangsan
'''

'''
match.txt
zhangsan 123456
lisi 456789
wangwu 789123
'''


import sys
account_file='D:\match.txt'
locked_file='D:\locked.txt'


def deny_account(username):
	print('您的账户已被锁定！')
	with file(lock_file,'a') as deny_f:
		deny_f.write('\n'+username)

def main():
    retry_count = 0
    retry_limit = 3

    while retry_count < retry_limit:
        username = input('请输入用户名：')
        with file(locked_file,'r') as lock_f:

        for line in lock_f.readlines():
            if len(line)==0:
                continue
            if username == line.strip():
                sys.exit('用户已被锁定' username) =

        if len(username)==0:
            print('用户名不能为空，请重新输入')
            continue

        passward = input('请输入密码：')
        with file(account_file,'r') as account_f:
            flag=False

            for line in account_f.readlines():
                user,pawd=line.strip().split()
                if username == user and passward ==pawd:
                    print("登录成功")
                    flag=True
                    break

        if flag==False:
            if retry_count < 2:
                print("您输入的密码有误，请重新输入！")

            retry_count+=1

sys
        else:
            break

    else:
        deny_account(username)



if __name__  ==  '__main__'
    main()


