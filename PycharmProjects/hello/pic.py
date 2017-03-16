#!/usr/bin/env python
# encoding: utf-8

"""
@version: Python 2.7
@author: Admin
@license: Apache Licence 
@contact: yang.hu@live.com
@software: PyCharm
@file: pic.py
@time: 2017/2/20 09:58
"""

import pickle

account_info = {
    '8908223632':['alex3714',15000,15000],
    '8908223631':['rachel',9000,9000],
    }
f = open('account.pkl','wb')
pickle.dump(account_info,f)
f.close()

#load data frist
pkl_file = open('account.pkl','rb')
account_list = pickle.load(pkl_file)
pkl_file.close()
print(account_info)
print(account_list)