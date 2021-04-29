import sqlite3

"""
・sqlite3 Download → URL:https://www.sqlite.org/download.html
展開して、anaconda3のScript配下に移動しておく
""" 

# DB NAME
TEST_DB = 'sqlite_test.db'

# SQL文
CREATE_SQL = 'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
INSERT_SQL = 'INSERT INTO persons(name) values("Yamada")'
UPDATE_SQL = 'UPDATE persons set name = "Shimada" where id = 3'
SELECT_SQL = 'SELECT * FROM persons'

#con = sqlite3.connect(TEST_DB)

# インメモリデータベース（実行後、消える）
con = sqlite3.connect(':memory:')

curs = con.cursor()

curs.execute(CREATE_SQL)
curs.execute(INSERT_SQL)
# curs.execute(UPDATE_SQL)
con.commit()

curs.execute(SELECT_SQL)
print(curs.fetchall())

con.close