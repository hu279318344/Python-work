# encoding=utf-8

#第一种方式

import mysql.connector

cnx = mysql.connector.connect(user='root', password='123456',
                              host='127.0.0.1',
                              database='db1')
cursor = cnx.cursor()
cursor.execute("use db1;")
cursor.execute("""CREATE TABLE `workers_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `workername` varchar(20) NOT NULL,
  `sex` enum('F','M','S'),
  `salary` int(11) DEFAULT '0',
  `email`  varchar(30),
  `EmployedDates`  date,
  `department`  varchar(30),
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;""")
data = cursor.fetchmany(10)
print data
cnx.close()
#第二种方式
'''
from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='scott', password='tiger',
                                 host='127.0.0.1',
                                 database='employees')
cnx.close()
'''
#第三种方式
'''
import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='scott',
                                database='testt')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()
'''
#第四种方式
'''
import mysql.connector

config = {
  'user': 'scott',
  'password': 'tiger',
  'host': '127.0.0.1',
  'database': 'employees',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)

cnx.close()
'''