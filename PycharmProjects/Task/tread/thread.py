#!/usr/bin/env python
# encoding: utf-8

"""
@version: Python 3.6
@author: Admin
@license: Apache Licence 
@contact: yang.hu@live.com
@software: PyCharm
@file: thread.py
@time: 2017/4/1 15:08
"""


import threading
import time

def run(num):
    print('Hi,I am thread %s ...' % num)
    time.sleep(1)
for i in range(20):
    t = threading.Thread(target=run,args=(i,))
    t.start()
    t.join()