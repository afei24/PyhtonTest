#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:afei  time:2018/11/29

"""
    正则表达式练习
"""

import re


content = '''Hello 1234567 World_This
is a Regex Demo
'''

result = re.match('^He.*?(\d+).*?Demo', content, re.S)

print(result.group(1))