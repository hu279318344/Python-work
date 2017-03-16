#!/usr/bin/env python
# encoding: utf-8

"""
@version: Python 3.6
@author: Admin
@license: Apache Licence 
@contact: yang.hu@live.com
@software: PyCharm
@file: sy.py
@time: 2017/2/22 16:37
linux run
"""


import  sys
print(sys.argv)

if '-h' or '-V' in sys.argv:
    host = sys.argv[sys.argv.index('-V')+1]
    print(host)