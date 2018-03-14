import copy
dic = {
    "CPU":[80,],
    "Mem":[80,],
    "Disk":[80,]
}

print("Old_Dic= ",dic)
print("Old_Dic id= ",id(dic))

print()
print()

NewDic = copy.copy(dic)
NewDic['CPU'][0] = 50

print('NewDic= ',NewDic)
print('NewDic id= ',id(NewDic))


print()
print()


print('dic= ',dic)
print('dic id= ',id(dic))


print(id(dic['CPU'][0]))
print(id[NewDic]['CPU'][0])
