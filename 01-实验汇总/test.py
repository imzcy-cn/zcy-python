def fetch(backend):
    backend_title = 'backend %s' % backend
    record_list = []
    with open('ha','r') as obj:
        flag = False
        for line in obj:
            line = line.strip()
            if line == backend_title:
                flag = True
            if flag and line.startswith(" "):
                flag = False
                break

            if flag and line:
                record_list.append(line)

    return record_list


#data = input("Please enter your data: ")
#fetch(data)


'''
if __name__ == '__main__':

    print('1、获取；2、添加；3、删除')
    num = input('请输入序号：')
    data = input('请输入内容：')
    if num == '1':
        fetch(data)
    else:
        dict_data = json.loads(data)
        if num == '2':
            add(dict_data)
        elif num == '3':
            remove(dict_data)
        else:
            pass
'''






'''
with open('ha','r') as zcy:
    for line in zcy:
        if line.startswith(" "):
            print(line)
'''




def zcy(ZhanDian):
    title = "backend %s" %ZhanDian
    MyList = []
    print(title)
    with open('ha','r') as obj:
        for line in obj:
            if line == title:
                print(line)
                print(line)
                MyList.append(line)
                while line.startswith(" "):
                    print(line)
                    MyList.append(line)
                break
            else:
                continue
    print(MyList)

data = input("请输入要查询的网址： ")
zcy(data)



