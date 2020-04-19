import sqlite3

fr = open("rank.csv","r")
ls = []
for line in fr:
    line = line.replace("\n","")
    ls.append(line.split(','))
fr.close()
#print(ls)
conn = sqlite3.connect('rank.db')
c = conn.cursor()
c.execute("CREATE TABLE rank("+ls[0][0]+ "  INT,"+ls[0][1]+  "  TEXT    NOT NULL,"+ls[0][2]+  "  INT,"+ls[0][3]+  "  INT)")

# 插入数据
c.executemany("insert into rank values(?,?,?,?)",ls[1:])
conn.commit()
