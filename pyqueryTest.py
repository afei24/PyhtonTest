#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:afei  time:2018/12/5


from pyquery import PyQuery as pq


html = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">thrid item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
doc = pq(html)
print(doc('li'))
