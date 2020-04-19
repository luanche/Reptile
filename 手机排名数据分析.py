import sqlite3
conn = sqlite3.connect('phonerank.db')

fr = open("phonerank.csv","r")
ls = []
for line in fr:
    line = line.replace("\n","")
    ls.append(line.split(','))
    print(line)
fr.close()
c = conn.cursor()

c.execute("CREATE TABLE rank("+ls[0][0]+ "  INT,"+ls[0][1]+ "   TEXT    NOT NULL," +ls[0][2]+  "  INT,"+ls[0][3]+  "  INT)")

c.executemany("insert into rank values(?,?,?,?)",ls[1:])
conn.commit()
