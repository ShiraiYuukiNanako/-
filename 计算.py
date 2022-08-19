import csv as c
右侧中线初始化=[]
左侧中线初始化=[]
左侧=[]
右侧=[]

with open("统计.csv") as g:
    g_csv = c.reader(g)
    for row in g_csv:
        左侧.append(row[0])
        右侧.append(row[1])

with open("中线初始化（右线）.csv") as f:
    f_csv = c.reader(f)
    for row in f_csv:
        右侧中线初始化.append(row)

with open("中线初始化（左线）.csv") as f:
    f_csv = c.reader(f)
    for row in f_csv:
        左侧中线初始化.append(row)

zc = []
for element in 左侧中线初始化:
    if element[0] in 左侧:
        zc.append(element)
    else:
        zc.append([element[0], 0, 0])

with open("左侧总表.csv","w") as t:
    w1 = c.writer(t)
    w1.writerows(zc)

yc = []
for element in 右侧中线初始化:
    if element[0] in 右侧:
        yc.append(element)
    else:
        yc.append([element[0], 0, 0])

with open("右侧总表.csv","w") as z:
    w2 = c.writer(z)
    w2.writerows(yc)



for item in 右侧:
    print(item+",", end = "")