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

cur.execute("INSERT INTO test (email, first_name, age) VALUES ('yeho@gmail.com', 'josh', 14)")

con.commit()

con.close()

print("hello world")