#另一种用户名匹配方式

lines=[]
for line in lock_f.readline():
    lines.append(line.strip())
if username in lines: