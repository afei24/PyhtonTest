#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:afei  time:2018/12/3

from bs4 import BeautifulSoup


soup = BeautifulSoup('<p>hello</p>', 'lxml')
print(soup.p.string)
