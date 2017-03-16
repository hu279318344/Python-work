#!/usr/bin/env python
# encoding: utf-8

"""
@version: Python 2.7
@author: Admin
@license: Apache Licence 
@contact: yang.hu@live.com
@software: PyCharm
@file: 进度条.py
@time: 2017/2/9 17:15
"""

import time

fmt = '{:3d} [{:<20}]'.format


def progressbar():
    for n in range(21):
        time.sleep(0.1)
        print '\r', fmt(n * 5, '=' * n),


progressbar()
print