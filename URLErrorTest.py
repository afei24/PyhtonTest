#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:afei  time:2018/11/25

import ssl
from urllib import request, error


ssl._create_default_https_context = ssl._create_unverified_context

try:
    response = request.urlopen('https://cuiqingcai.com/index.html')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
