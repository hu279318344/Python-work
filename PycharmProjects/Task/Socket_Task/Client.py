#!/usr/bin/env python
# encoding: utf-8

"""
@version: Python 3.6
@author: Admin
@license: Apache Licence 
@contact: yang.hu@live.com
@software: PyCharm
@file: Client.py
@time: 2017/3/8 15:38
"""


import socket

HOST = '127.0.0.1'
PORT = 50007
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

#first_header = 'Hello'
#following_header = 'World'
#data = "%s\r\n%s\r\n\r\n" % (first_header, following_header)
#s.sendall(data.encode(encoding='utf-8'))

#s.sendall ( ('Hello world').encode ( encoding='utf-8' ) )

while True:
    user_input = str(input("Msg to send::").strip())
    if len(user_input) == 0:
        continue
    else:
        s.send((user_input).encode ( encoding='utf-8' ))
        data = s.recv(1024)
        print ( 'Received,%s' % (data))
s.close()
