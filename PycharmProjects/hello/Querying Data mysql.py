#!/usr/bin/env python
# encoding: utf-8

"""
@version: Python 2.7
@author: Admin
@license: Apache Licence 
@contact: yang.hu@live.com
@software: PyCharm
@file: Querying Data mysql.py
@time: 2017/1/17 14:10
"""


import datetime
import mysql.connector

config = {
  'user': 'root',
  'password': '123456',
  'host': '127.0.0.1',
  'database': 'db1',
  'raise_on_warnings': True,
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = ("SELECT first_name, last_name,birth_date,hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(1900, 1, 1)
hire_end = datetime.date(2020, 12, 31)

cursor.execute(query, (hire_start, hire_end))

for (first_name, last_name, birth_date,hire_date) in cursor:
  print("{}, {} Birth day on {:%d %b %Y},was hired on {:%d %b %Y}\n".format(
    last_name, first_name, birth_date,hire_date))

  print (''' Information of the company Employees:
            Last_Name : %s
            First_Name: %s
            Birth_date: %s
            hire_date : %s
             ''' % (last_name, first_name, birth_date,hire_date))


'''
birth = ("SELECT first_name, last_name, birth_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")
cursor.execute(birth, (hire_start, hire_end))

for (first_name, last_name, birth_date) in cursor:
  print("{}, {} was Birth day on {:%d %b %Y}".format(
      last_name, first_name, birth_date))
'''
cursor.close()
cnx.close()