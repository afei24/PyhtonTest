#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:afei  time:2018/12/8

import pymysql


db = pymysql.connect(host='localhost', user='root', password='lpf123456', port=3306, db='spiders')
cursor = db.cursor()
# cursor.execute('select version()')
# data = cursor.fetchone()
# print('Database version:', data)
# cursor.execute('create database spiders default  character  set utf8')

'''
sql = 'create table if not exists students (id varchar (255) not null, ' \
      'name varchar(255) not null, age int not null, primary  key (id))'
cursor.execute(sql)
'''

id = '20120001'
user = 'Bob'
age = 20

sql = 'insert into students(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql,(id,user,age))
    db.commit()
except:
    db.rollback()

db.close()
