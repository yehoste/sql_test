import sqlite3

con=sqlite3.connect("test.db")

cur=con.cursor()

# cur.execute("""--sql
#     CREATE TABLE IF NOT EXISTS test(
#         email text PRIMARY KEY,
#         first_name text,
#         age integer
#     )
#     """)

# cur.execute("INSERT INTO test (email, first_name, age) VALUES ('yeho@gmail.com', 'josh', 14)")

cur.execute("SELECT * FROM test")
db=cur.fetchall()
print(db)

print(db[0][2])

print(type(db[0][2]))

for row in db:
    print(row)

cur.execute("SELECT first_name,age FROM test WHERE age IS 19")

print(cur.fetchall())

cur.execute("SELECT email FROM test WHERE email LIKE 'yeho%' ")

print(cur.fetchall())

# cur.executemany("INSERT INTO test VALUES (?,?,?)", [('yeho4@gmail.com','yeho1',19)])

con.commit()




#update db


cur.execute("""--sql
        UPDATE test SET first_name = 'yeho'
        WHERE email LIKE 'yeho%'

    """)


con.commit()

cur.execute("DELETE FROM test WHERE rowid=6")
con.commit()






con.close()

print("hello world")