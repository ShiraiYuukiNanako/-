import csv as c
左侧=[]
右侧=[]

with open("统计.csv") as g:
    g_csv = c.reader(g)
    for row in g_csv:
        左侧.append(row[0])
        右侧.append(row[1])

右线 = []
with open("中线初始化（右线）.csv") as y:
    y_csv = c.reader(y)
    for row in y_csv:
        if row[0] in 右侧:
            右线.append(row[0])

左线 = []
with open("中线初始化（左线）.csv") as y:
    y_csv = c.reader(y)
    for row in y_csv:
        if row[0] in 左侧:
            左线.append(row[0])

for item in 左线:
    print(item+",", end = "")