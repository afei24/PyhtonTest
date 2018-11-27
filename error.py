#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:afei  time:2018/11/25

import socket
import urllib.request
import urllib.error


try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    print('TIME OUT1')
    '''
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
    '''
except socket.timeout as e:
    print(e)


