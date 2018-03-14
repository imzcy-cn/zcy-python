import copy


dic = {
    "cpu" : [80,],
    "mem":[80,],
    "disk":[80,]
}
print(dic.items())

def ZCY_QianCopy():
    NewDic = copy.copy(dic)
    NewDic['cpu'][0] = 50
    print(dic)
    print(NewDic)


def ZCY_ShenCopy():
    NewDic2 = copy.deepcopy(dic)
    NewDic2['cpu'][0] = 50
    print(dic)
    print(NewDic2)

ZCY_QianCopy()
ZCY_ShenCopy()


有问题，还需修改
