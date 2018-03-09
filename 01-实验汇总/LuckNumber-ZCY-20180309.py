#设置一个幸运数字，，获取用户输入数字；如用户输入数字大于幸运数字，提示用户输入小一点；如果用户输入数字小于幸运数字，提示用户输入大一点；如果用户输入为幸运数字，提示Bingo


LuckNumber = 8
GuessCount = 0

while GuessCount < 3:
    InputNumber = int(input("Please input your number: "))
    if InputNumber > LuckNumber:
        print("再小一点.")
    elif InputNumber < LuckNumber:
        print("再大一点")
    else:
        print("Bingo!")
        break
    GuessCount += 1
else:
    print("输入次数太多！.")




zhushi = '''
最后的一个else表示前面while循环正常退出则执行else后面内容，
    如果while不正常退出（例如break退出），则不会执行else后面内容


常用的数据类型：
int 整数
float 浮点数
long 长整数（后面跟L）

可用type() 来查看数据类型

'''