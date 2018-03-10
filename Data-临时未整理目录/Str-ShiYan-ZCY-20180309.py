



'''
name = input("Please input your name: ").strip()
age = input("Please input your age: ")
job = input("Please input your job: ").strip("T")


msg = '''
Information3 of %s:
    Name:%s
    Age:%s
    Job:%s
''' %(name,name,age,job)

print(msg)

'''



zhushi = '''
    移除空白：
        input()后面加.strip() 表示去除输入的字符串两端的空格
        .strip("T") 表示去除输入中字符串两端包含的字符T
        .strip("n" + "z") 表示去除字符串两端的n和z字符
    分割：

'''