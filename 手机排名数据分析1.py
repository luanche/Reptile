import sqlite3

conn = sqlite3.connect('phonerank.db')
c = conn.cursor()
c.execute('SELECT * from rank where 评分 >= 9')
lines = c.fetchall()
for line in lines:
    for item in line:
        print(item,end='\t')
    print()
