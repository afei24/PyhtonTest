#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:afei  time:2018/12/11

import pymongo


client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students
