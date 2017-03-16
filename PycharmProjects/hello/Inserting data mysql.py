#!/usr/bin/env python
# encoding: utf-8

"""
@version: Python 2.7
@author: Admin
@license: Apache Licence 
@contact: yang.hu@live.com
@software: PyCharm
@file: Inserting data mysql.py
@time: 2017/1/17 14:05
"""

from __future__ import print_function
from datetime import date, datetime, timedelta
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

tomorrow = datetime.now().date() + timedelta(days=1)

add_employee = ("INSERT INTO employees "
               "(first_name, last_name, hire_date, gender, birth_date) "
               "VALUES (%s, %s, %s, %s, %s)")
add_salary = ("INSERT INTO salaries "
              "(emp_no, salary, from_date, to_date) "
              "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))

# Insert new employee
cursor.execute(add_employee, data_employee)
emp_no = cursor.lastrowid

# Insert salary information
data_salary = {
  'emp_no': emp_no,
  'salary': 50000,
  'from_date': tomorrow,
  'to_date': date(9999, 1, 1),
}
cursor.execute(add_salary, data_salary)

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()