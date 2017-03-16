#!/usr/bin/env python
# encoding: utf-8

"""
@version: Python 2.7
@author: Admin
@license: Apache Licence 
@contact: yang.hu@live.com
@software: PyCharm
@file: def.py
@time: 2017/2/10 14:41
"""


def sayHi(a,b):
    if a > 28 and b == 'yanghu':
        print '%s Time to get Married!' % a
    else:
        print 'Hey,You are stll young,enjoy you lisfe and do not waste it!'

name = str(raw_input('Pleas input you Name:')).split()
age = int(raw_input('Pleas input you age: '))
sayHi(age,name)