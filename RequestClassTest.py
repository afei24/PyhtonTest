#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:afei  time:2018/11/25

import urllib.request
import ssl
import urllib.parse

# ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://httpbin.org/post'
headers = {
    'User_Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
request = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))