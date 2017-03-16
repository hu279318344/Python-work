#!/usr/bin/env python
# encoding: utf-8

"""
@version: Python 2.7
@author: Admin
@license: Apache Licence 
@contact: yang.hu@live.com
@software: PyCharm
@file: file.py
@time: 2017/2/4 09:43
"""

import fileinput
import os

print os.getcwd()
print os.listdir('D:')
print os.name
print os.path.getsize('user.txt')


#Global replacement 全局替换
for line in fileinput.input('user.txt',inplace=1):
         line = line.replace('005','aaaa')
         print line,


