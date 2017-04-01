#!/usr/bin/env python
# encoding: utf-8

"""
@version: Python 3.6
@author: Admin
@license: Apache Licence 
@contact: yang.hu@live.com
@software: PyCharm
@file: tread2.py
@time: 2017/4/1 15:21
"""

import  threading
import time

class MyThread(threading.Thread):
    def_init_(self,name)
    threading.Thread.__init__(self)
    self.name = name

def run(self):
    print('Hi ,Iam threda',self.name)
    time.sleep(2)

for i in rang(10):
    t = MyThread(i)
    t.start()








