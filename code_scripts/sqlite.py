import sqlite3
import pandas as pd

conn = sqlite3.connect("DB1.db")
c = conn.cursor()

c.execute("INSERT INTO tab1 VALUES (1,'Ashutosh',79)")
c.execute("INSERT INTO tab1 VALUES (1,'Ashutosh',78)")

df1 = pd.read_sql_query("SELECT * from tab1", conn)

print(df1)

conn.commit()
conn.close()
