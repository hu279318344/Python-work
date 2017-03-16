#!/usr/bin/env python
# encoding: utf-8

"""
@version: Python 3.6
@author: Admin
@license: Apache Licence 
@contact: yang.hu@live.com
@software: PyCharm
@file: Service.py
@time: 2017/3/8 16:57
"""


import socketserver
import subprocess
import time

class MySocketServer(socketserver.BaseRequestHandler):

    def handle(self):
        print('Got a new conn from',self.client_address)
        while True:
            cmd = self.request.recv(4096).strip()
            if not cmd:
                print('Lost Connection with',self.client_address)
                break
            cmd_result = subprocess.getstatusoutput(cmd)

            #send result size
            self.request.send(str(len(cmd_result[1])).encode())
            time.sleep(0.2)
            #send result
            self.request.send((cmd_result[1]).encode())

            print(type(cmd_result))
            print(cmd_result)
            print(len(cmd_result[1]))


if __name__ == '__main__':
    HOST,PORT = '0.0.0.0', 50007
    print('MySocketServer is Runing; Host=%s; Port=%s ... ...' % (HOST, PORT))
    server = socketserver.ThreadingTCPServer((HOST,PORT),MySocketServer)
    server.serve_forever()
