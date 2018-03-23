ShangPin = [
    ('iphone',5000),
    ('MacBook Pro',10000),
    ('方便面',6),
    ('火腿肠',2),
    ('辣条',0.5)
]

GongZi = input("请输入您的工资： ")
shopping_list = []
if GongZi.isdigit():
    GongZi = int(GongZi)
    while True:
        for index,item in enumerate(ShangPin):
            print(index,item)
        XuanZe = input("选择要买什么？ >>>")
        if XuanZe.isdigit():
            XuanZe = int(XuanZe)
            if XuanZe < len(ShangPin) and XuanZe >= 0:
                P_Item = ShangPin[XuanZe]
                if P_Item[1] <= GongZi:
                    shopping_list.append(P_Item)
                    GongZi -= P_Item[1]
                    print("添加[ %s ]到购物车中，您的当前工资为 \033[31;1m%s\033[0m" %(P_Item[0],GongZi))
                else:
                    print("\033[41;2m您的余额只剩%s,买不起该商品\033[0m" %GongZi)
            else:
                print("请输入正确的商品编号！")

        if XuanZe == 'q':
            if len(shopping_list) == 0:
                print("您没有购买任何商品，当余额为 %s" %GongZi)
                exit(1)
            else:
                print("一共购买了%s，余额为%s" %(shopping_list,GongZi))
                exit(1)

