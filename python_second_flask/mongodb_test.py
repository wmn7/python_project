from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
db = client.shiyanlou

# 查找数据
for user in db.user.find():
    print(user)
    print(type(user))

print("-------------")

sel = db.user.find({'name': "jin"})
result = []
for x in sel:
    result.append(x)

print(result)

print("-------------")

print(db.user.find_one({'name':"jin"}))

#插入数据
user = {'name': 'Aiden', 'age': 30, 'addr': ['CD', 'SH', 'BJ']}
db.user.insert_one(user)

print(db.user.find_one({'name': 'Aiden'}))

#更新数据库
db.user.update_one({'name': 'Aiden'}, {'$set': {'email': 'aiden@simplecloud.cn'}})

use = db.user.find_one({'name': 'Aiden'})
print(use)

print(use['name'])