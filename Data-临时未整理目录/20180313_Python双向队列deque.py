'''
单向队列    先进先出
栈          后进先出
'''





'''双向队列方法：
append()            往右边添加
appendleft()        往左边添加
clear()             清空
count()             看队列某个元素出现多少次
extend()            扩展（多个元素一下放进来）
extendleft()        左边扩展
index()             取值的索引位置
insert()            插入
pop()               默认从右边去
popleft()           往左边去
remove()            删除某些值
reverse()           反转
rotate()            从右边拿数据插入到左边（可以指定拿的个数，最后拿的(之前中间位置的)数据在最左边）


'''

import collections

def ZCY_Deque():
    d = collections.deque()
    d.append(1)
    d.appendleft(10)
    d.appendleft(2)
    d.append(1)
    print(d.count(1))
ZCY_Deque()


