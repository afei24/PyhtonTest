#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:afei  time:2018/12/13


from redis import StrictRedis


redis = StrictRedis(host='localhost', port=6379, db=0)
redis.set('name', 'Bob')
print(redis.get('name'))
