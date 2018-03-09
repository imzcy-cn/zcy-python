name = input("Please input your name: ")
age = input("Please input your age: ")
job = input("Please input your job: ")


#第一种方法：
print("Information1 of " + name + "\nName:" + name + "\nAge:" + age + "\nJob:" + job)


#第二种方法：
print("Information2 of %s:\nname:%s\nage:%s\njob:%s" %(name,name,age,job))


#第三种方法：(推荐这种)
msg = '''
Information3 of %s:
    Name:%s
    Age:%s
    Job:%s
''' %(name,name,age,job)

print(msg)





zhushi = '''
    %s 表示字符串
    %d 表示整数
    %f 表示浮点数

'''