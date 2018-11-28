#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:afei  time:2018/11/27

import requests
from  requests_oauthlib import  OAuth1

'''
proxies = {
    'http': 'socks5://18363001105lu:lpf137724742@10.10.1.10:3128',
    'https': 'socks5://18363001105lu:lpf137724742@10.10.1.10:3128',
}

response = requests.get("https://www.taobao.com", proxies)
print(response.text)

'''


url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('key', 'secret', 'token', 'token_secret')
response = requests.get(url, auth=auth)
print(response.status_code)
