#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function

"""
@version: Python 2.7
@author: Admin
@license: Apache Licence 
@contact: yang.hu@live.com
@software: PyCharm
@file: Dictionaries.py
@time: 2017/2/10 10:33
"""

Dictionaries = dict(yanghu=["15201095980,It,28"], raln="18234556789", zhangsan="13335678900")
Dictionaries["lisi"] = '15298703456'
Dictionaries["ran"] = '123456'

for k,v in Dictionaries.items():
    print (k,v)
    if type(v) is list:
        for p in v:

            print  (k,p)
    else:
        print (k,v)
print (Dictionaries.get("yanghu"))
print (Dictionaries.keys())
print (Dictionaries)