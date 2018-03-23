ShangPin = [
    ('iphone',5000),
    ('MacBook Pro',10000),
    ('方便面',6),
    ('火腿肠',2),
    ('辣条',0.5)
]
YuE = input("请输入您的工资： ")
if YuE.isdigit():
    YuE = int(YuE)
    while True:
        for index,item in enumerate(ShangPin,start=1):
            print(index,item)
        GouWu = input("请输入要购买的商品编号：")
        if GouWu.isdigit():
            GouWu = int(GouWu)
            if GouWu < 6:
                
                print("能买")
            else:
                print("您的余额为%s,买不起了。。。" %YuE)



