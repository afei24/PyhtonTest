#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:afei  time:2018/12/11

import pymongo


client = pymongo.MongoClient(host='localhost', port=27017)
db = client.taobao
collection = db.products

'''
student = {
    'id':'20181215',
    'name': 'Bob'
}

result = collection.insert_one(student)
print(result)
'''

results = collection.find()
for result in results:
    print(result)
