import sqlite3
conn=sqlite3.connect('Mid-morning')
print("Open database successfully")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL,GENDER)VALUES(1,'Marcus',23,'eMobilis','male')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL,GENDER)VALUES(2,'Masek',40,'eMobilis','male')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL,GENDER)VALUES(3,'Mark',12,'eMobilis','male')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL,GENDER)VALUES(4,'Marvin',67,'eMobilis','male')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL,GENDER)VALUES(5,'Timo',9,'eMobilis','male')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL,GENDER)VALUES(6,'JJ',99,'eMobilis','male')")


conn.commit()
print("Records added successfully")
