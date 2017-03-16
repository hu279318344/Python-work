#!/usr/bin/env python
# encoding: utf-8

"""
@version: Python 2.7
@author: Admin
@license: Apache Licence 
@contact: yang.hu@live.com
@software: PyCharm
@file: list.py
@time: 2017/2/9 09:03
"""

name_list = []
name_list.append('yanghu')
name_list.append('zhangpeng')

name_list.insert(0,'aaa')
print  len(name_list)
print name_list
#print name_list[1]
for i in range(len(name_list)):
    print name_list[i]
name_list.pop()
print name_list
a = '1 2 3 w s d f qwe asdf er dfa '
a.split()
print a.split()
for name in a.split():
    print name
