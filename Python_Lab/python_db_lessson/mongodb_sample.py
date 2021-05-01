"""
#############################################################################
ドキュメント型NoSQLデータベース：MongoDB
　・JSON形式でデータを格納
　・ログなどの用途で利用：高速
 mongod --dbpath .\Python_Lab\python_db_lessson\mongodata\db\
#############################################################################

"""

import datetime

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_mongo_db']

stack1 = {
    'name': 'user1',
    'pip': ['python', 'java', 'go'],
    'info': {'os': 'mac'},
    'data': datetime.datetime.utcnow()
}

stack2 = {
    'name': 'user2',
    'pip': ['python', 'java'],
    'info': {'os': 'windows'},
    'data': datetime.datetime.utcnow()
}

db_stacks = db.stacks

#データのインサート
stack_id1 = db_stacks.insert_one(stack1).inserted_id
stack_id2 = db_stacks.insert_one(stack2).inserted_id
print(stack_id1, type(stack_id1))
print("########################")

#上記で取得したstack_idのデータを取得する
print(db_stacks.find_one({'_id': stack_id1}))

print(db_stacks.find_one({'name': 'user2'}))

# 全データを取得する
for stack in db_stacks.find():
    print(stack)
    
# 現時刻より前のデータを取得する
now = datetime.datetime.utcnow()
for stack in db_stacks.find({'data': {'$lt': now}}):
    print(stack)

 