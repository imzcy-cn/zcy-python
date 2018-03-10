'''List支持的方法
dir(NameList)   列出NameList所能操作的所有方法

append          追加              >> > NameList.append("lisi")
count           统计              >> > NameList.count('lisi')
extend          扩展              >> > NameList.extend(a)
index           索引              >> > NameList.index('lisi')
insert          插入              >> > NameList.insert(2, 'lisi2')
pop             删除一个          >> > NameList.pop()
remove          删除指定的一个    >> > NameList.remove('lisi2')
reverse         反转              >> > NameList.reverse()
sort            排序              >> > NameList.sort()
'''







'''索引：
        >> > NameList = ['zhangsan', 'lisi', 'wanger']          # 定义列表NameList的三个元素['zhangsan','lisi','wanger']
        >> > NameList
        ['zhangsan', 'lisi', 'wanger']
        >> > NameList[0]                                        # 取出列表NameList中索引为0的元素
        'zhangsan'
        >> > NameList[1]                                        # 取出列表NameList中索引为1的元素
        'lisi'

索引在pytho中又称为下标
'''






'''切片：
    >> > NameList = [6, 5, 4, 3, 2, 1]
    >> > NameList
    [6, 5, 4, 3, 2, 1]
    >> > NameList[0:2]
    [6, 5]
    >> > NameList[0:6]
    [6, 5, 4, 3, 2, 1]
    >> > NameList[2:6]
    [4, 3, 2, 1]
    >> > NameList[0:6:2]
    [6, 4, 2]
    >> > NameList[0:6:3]
    [6, 3]
    >> > NameList[-2:]
    [2, 1]
    >> > NameList[:3]
    [6, 5, 4]
'''





'''包含：
    >> > NameList
    [6, 5, 4, 3, 2, 1, 'c', 'b', 'a']
    >> > if 1 in NameList:
        ...
        print("bao han")
    ...
    bao
    han
    >> >
'''



