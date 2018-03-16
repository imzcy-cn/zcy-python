'''


'''


#一个*把传入的所有参数，自动转换为元祖（元祖的元素只有一个的时候，需要再后面加一个,逗号）
def ZCY_T(*aa):
    print(aa)
#ZCY_T(123,456)



#两个*把传入的所有参数，自动转换为字典（要注意传入参数的格式a=123 ，需要有key和value）
def ZCY_D(**aa):
    print(aa)
#ZCY_D(a=123,b=456)




#一个*和两个*结合(一个*的必须放在前面，不然语法会报错)
def ZCY_T_D(*aa,**bb):
    print(aa,type(aa))
    print(bb,type(bb))
ZCY_T_D(11,22,33,A=44,B=55)



