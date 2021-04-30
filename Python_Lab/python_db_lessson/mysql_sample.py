import mysql.connector

# MySQL user
USER = 'root'
PASSWORD = 'tsujiba'

"""
#############################################################################
データベースを作成する
※一度作成したらコメントアウトする
mysql>show database;で確認できる
#############################################################################

"""
# SQL文
CREATE_DB = 'CREATE DATABASE test_mysql_database'

# conn = mysql.connector.connect(host='127.0.0.1', user=USER, password=PASSWORD)

# cursor = conn.cursor()

# cursor.execute(CREATE_DB)

# cursor.close()
# conn.close()

"""
#############################################################################
作成したデータベースへ接続する
データベースにテーブルを作成する
※一度作成したらコメントアウトする
mysql>use test_mysql_database;でデータベースを使用できる
mysql>show create tables persons;でテーブルを確認
#############################################################################

"""
# CREATE_TABLE = 'CREATE TABLE persons(id int NOT NULL AUTO_INCREMENT, name varchar(14) NOT NULL, PRIMARY KEY(id))'

# DBNAME = 'test_mysql_database'

# conn = mysql.connector.connect(host='127.0.0.1', database=DBNAME, user=USER, password=PASSWORD)

# cursor = conn.cursor()

# cursor.execute(CREATE_TABLE)
# conn.commit()

# cursor.close()
# conn.close()

"""
#############################################################################
作成したデータベーステーブルに値をインサートする
作成したデータベーステーブルに値をアップデートする
作成したデータベーステーブルに値を削除する
#############################################################################

"""
# INSERT_SQL1 = 'INSERT INTO persons(name) value("Tsujiba")'
# INSERT_SQL2 = 'INSERT INTO persons(name) value("Yamada")'
# UPDATE_SQL = 'UPDATE persons set name = "Tanaka" where id = 1'
# DELETE_SQL = 'DELETE FROM persons where name = "Tanaka"'
# SELECT_SQL = 'SELECT * FROM persons'

# DBNAME = 'test_mysql_database'

# conn = mysql.connector.connect(host='127.0.0.1', database=DBNAME, user=USER, password=PASSWORD)

# cursor = conn.cursor()

# # cursor.execute(INSERT_SQL1)
# # cursor.execute(INSERT_SQL2)
# # cursor.execute(UPDATE_SQL)
# # cursor.execute(DELETE_SQL)
# # conn.commit()

# cursor.execute(SELECT_SQL)
# for row in cursor:
#     print(row)
    
# cursor.close()
# conn.close()

"""
#############################################################################
テーブルを削除する
#############################################################################

"""

DELETE_TABLE = 'DROP TABLE persons'

DBNAME = 'test_mysql_database'

conn = mysql.connector.connect(host='127.0.0.1', database=DBNAME, user=USER, password=PASSWORD)

cursor = conn.cursor()

cursor.execute(DELETE_TABLE)
    
cursor.close()
conn.close()

