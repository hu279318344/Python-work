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

HOST = '192.168.0.186'
PORT = 50007
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

def recv_all(obj,msg_length):
    raw_result = ''
    data    =''
    while msg_length !=0:
        if msg_length <= 4096:
            data = str(obj.recv(msg_length).decode())
            msg_length = 0
        else:
            data = str(obj.recv(4096).decode())
            msg_length -= 4096
        raw_result += data
    return raw_result

while True:
    user_input = str(input("Msg to send:").strip())
    if len(user_input) == 0:
        continue
    else:
        s.send((user_input).encode())

        recv_size = s.recv(4096)
        recv_data = recv_all(s,int(recv_size))
        #recv_size = s.recv(4096).decode()
        #recv_date = s.recv(int(recv_size)).decode()
        if not recv_data:
            break
        print('LEN(recv_size) is %s' % recv_size)
        print('Received,%s' % recv_data)
        print(type(recv_data))
s.close()
