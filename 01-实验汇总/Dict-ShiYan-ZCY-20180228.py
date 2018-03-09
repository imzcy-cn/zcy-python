import os
import sys

DiFang = {
    "北京市":{
        "东城区":{
            "东城区景点1":"东城区景点",
            "东城区景点2":"东城区景点",
            "东城区景点3":"东城区景点"
        },
        "西城区":{
            "西城区景点1":"西城区景点",
            "西城区景点2":"西城区景点",
            "西城区景点3":"西城区景点"
        },
        "朝阳区":{
            "朝阳区景点1":"朝阳区景点",
            "朝阳区景点2":"朝区景点",
            "朝阳区景点3":"朝阳区景点"
        }
    },
    "上海市":{
        "黄浦区":{
            "黄浦区景点1":"黄浦区景点",
            "黄浦区景点2":"黄浦区景点",
            "黄浦区景点3":"黄浦区景点"
        },
        "虹口区":{
            "虹口区景点1":"虹口区景点",
            "虹口区景点2":"虹口区景点",
            "虹口区景点3":"虹口区景点"
        },
        "长宁区":{
            "长宁区景点A":"长宁区景点",
            "长宁区景点B":"长宁区景点",
            "长宁区景点C":"长宁区景点"
        }
    },
    "广州市":{
        "天河区":{
            "天河区景点1":"天河区景点",
            "天河区景点2":"天河区景点",
            "天河区景点3":"天河区景点"
        },
        "白云区":{
            "白云区景点1":"白云区景点",
            "白云区景点2":"白云区景点",
            "白云区景点3":"白云区景点"
        }
    }
}


l1 = False
l2 = False
l3 = False

while l1 == False:
    for A in DiFang.keys():
        print(A)
    AI = input("请输入要去的城市(输入Q退出程序)：")
    if AI == "Q":
        sys.exit(0)
    for Z in DiFang.keys():
        if AI in Z:
            break
    else:
        print("请输入正确的城市名！")
        continue
    while l2 == False:
        for B in DiFang[AI].keys():
            print(B)
        BI = input("请输入要去的区(输入Q退出程序，输入B返回上一层): ")
        if BI == "Q":
            sys.exit(0)
        if BI == "B":
            break
        for C in DiFang[AI].keys():
            if BI in C:
                break
        else:
            print("请输入正确的区名！")
            continue
        while l3 == False:
            for C in DiFang[AI][BI].keys():
                print(C)
            CI = input("输入B返回上一层，输入Q退出程序.")
            if CI == "Q":
                sys.exit(0)
            if CI == "B":
                break
            else:
                print("请输入正确的操作符（B返回，Q退出）")
                continue