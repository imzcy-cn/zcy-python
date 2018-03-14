





'''
qsize()             队列里元素的个数
full()              队列是否填满

'''


#首先导入queue模块
import queue

q = queue.Queue()
q.put('a')
q.put('b')
print(q.qsize())
print(q.get())              #因为单向队列先进先出，所有不用指定其他，get直接输出第一个添加的元素



