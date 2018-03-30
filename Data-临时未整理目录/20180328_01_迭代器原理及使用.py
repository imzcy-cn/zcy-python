'''生成一个迭代器


'''


name1 = ['zhangsan','lisi','wangwu']
name2 = iter(['zhangsan','lisi','wangwu'])

print('打印列表name1的值为',name1)

print("迭代器的第一个元素的值为",name2.__next__())
print("迭代器的第二个元素的值为",name2.__next__())
print("迭代器的第三个元素的值为",name2.__next__())



