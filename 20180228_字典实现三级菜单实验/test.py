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


#while True:
a = input("请输入城市名：")
for k in DiFang.keys():
    if a in k:
        print("存在该城市")
        break
#if CS == True:
#   print("存在该城市")

print("123")
#else:
#    print("请输入正确城市名")
