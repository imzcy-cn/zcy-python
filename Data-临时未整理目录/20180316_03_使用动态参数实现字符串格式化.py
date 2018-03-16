'''


'''

#
S1 = "{0} is {1}"
A = ['zcy','ok']

bb = S1.format(*A)
print(bb)





#
S1 = "{name} is {acter}"
d = {'name':'zcy','acter':'ok'}
result = S1.format(name='zcy',acter='ok')
print(result)




#
S1 = "{name} is {acter}"
d = {'name':'zcy','acter':'ok'}
result = S1.format(**d)
print(result)








