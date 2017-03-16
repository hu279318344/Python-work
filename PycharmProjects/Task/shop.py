#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function

"""
@version: Python 2.7
@author: Admin
@license: Apache Licence 
@contact: yang.hu@live.com
@software: PyCharm
@file: shop.py
@time: 2017/2/10 09:51
"""

products = []
prices = []

f = file('shops.txt')
for line in f.readlines():
    p = line.split()[0]
    price = line.split()[1]
    products.append(p)
    prices.append(price)
print (products)
print (prices)
