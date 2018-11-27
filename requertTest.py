#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:afei  time:2018/11/25


import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

data = bytes(urllib.parse.urlencode({'world': 'hello'}), encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data)
print(response.read().decode('utf-8'))
