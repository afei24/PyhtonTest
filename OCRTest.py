#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:afei  time:2018/12/18

import locale
locale.setlocale(locale.LC_ALL, 'C')
from PIL import Image
import tesserocr

image = Image.open('Code.jpg')
result = tesserocr.image_to_text(image)
print(result)
