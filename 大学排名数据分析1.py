import sqlite3

conn = sqlite3.connect('rank.db')
c = conn.cursor()
c.execute('SELECT 排名,学校名称,省份,总分,max(培养规模) from rank')
lines = c.fetchall()
for line in lines:
    for item in line:
        print(item,end='\t')
    print()
