#!/usr/bin/env python
# encoding: utf-8

"""
@version: Python 3.6
@author: Admin
@license: Apache Licence 
@contact: yang.hu@live.com
@software: PyCharm
@file: Server_1.py
@time: 2017/3/8 15:34
"""


import  socket

HOST = '127.0.0.1'
PORT = 50007
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(10)
conn,addr = s.accept()
print('Connected by',addr)

while True:
    print ( 'Got a connection from' , addr)
    data = conn.recv(1024)
    if not data:
         break
    conn.send(data.upper())

    print('Received ...:',data)
conn.close()