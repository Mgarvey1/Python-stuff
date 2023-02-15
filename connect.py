import sqlite3
conn=sqlite3.connect('Mid-morning')
print("open database successfully")
conn.executive("CREATE TABLE Students")