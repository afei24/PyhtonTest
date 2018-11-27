#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:afei  time:2018/11/26

from urllib.parse import urlparse


result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)