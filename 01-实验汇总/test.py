def zcy(a):
    MyList = []
    Title = "backend %s" % a
    with open("ha",'r') as obj:
        flag = False
        for line in obj.readlines():
            line = line.strip()
            if line == Title:
                flag = True
                continue
            if flag and line.startswith("backend"):
                flag = False
                break
            if flag:
                MyList.append(line)
    print(*MyList,sep='\n')




data = input("data: ")
zcy(data)
