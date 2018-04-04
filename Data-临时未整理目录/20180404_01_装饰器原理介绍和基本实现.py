def login(func):
    print("验证身份")
    return func
    #return None

def tv():
    print("欢迎 [%s] 来到TV页面")

tv = login(tv)
tv()




