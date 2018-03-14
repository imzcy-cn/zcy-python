import copy
dic = {
    "CPU":'80',
    "Mem":'80',
    "Disk":["aa",'bb']
}


print('原始字典= ',dic)
print('原始字典ID= ',id(dic))
print('原始字典的Disk的ID= ',id(dic['Disk']))

'''
NewDic = copy.copy(dic)
NewDic['Disk'][0] = 50

print(NewDic)
print('NewDic字典的Disk的ID= ',id(NewDic['Disk']))
print(dic)
print('原始Dic字典的Disk的ID= ',id(dic['Disk']))                  #浅拷贝原始字典的Disk键值的ID和NewDic的Disk键值的ID相同
                                                                 #浅拷贝只拷贝第一层，所以有多层元素，，修改新字典包含多层元素的键，因为是相同ID，所以等于原始数据也被修改了

D:\1_zcy_data\0_zcy_python\1_python_MianAnZhuangJieShiChengXu\python-3.6.3-embed-amd64\python.exe D:/1_zcy_data/0_zcy_python/0_pycharm_data/zcy-python/Data-临时未整理目录/test.py
原始字典=  {'CPU': '80', 'Mem': '80', 'Disk': ['aa', 'bb']}
原始字典ID=  2173788089008
原始字典的Disk的ID=  2173788698888
{'CPU': '80', 'Mem': '80', 'Disk': [50, 'bb']}
NewDic字典的Disk的ID=  2173788698888
{'CPU': '80', 'Mem': '80', 'Disk': [50, 'bb']}
原始Dic字典的Disk的ID=  2173788698888
'''




NewDic = copy.deepcopy(dic)
NewDic['Disk'][0] = 50


print('NewDic的值为= ',NewDic)
print('NewDic的Disk元素的ID= ',id(NewDic['Disk']))

print('原始Dic字典的值为= ',dic)
print('原始字典的Disk的ID为= ',id(dic['Disk']))                    #深拷贝原始Disk和NewDic的ID不相同




