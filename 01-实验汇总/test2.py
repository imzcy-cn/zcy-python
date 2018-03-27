import json
import os

def fetch(backend):
    backend_title = 'backend %s' % backend
    record_list = []
    with open('ha') as obj:
        flag = False
        for line in obj:

            line = line.strip()
            print("line1= ",line)
            if line == backend_title:
                print("line2=",line)
                flag = True
                continue
            if flag and line.startswith('backend'):
                flag = False
                break
            if flag and line:
                record_list.append(line)

        #return record_list


data = input("请输入查询到站点： ")
fetch(data)