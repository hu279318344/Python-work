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

class MySocketServer(socketserver.BaseRequestHandler):

    def handle(self):
        print('Got a new conn from',self.client_address)
        while True:
            data = self.request.recv(1024).strip()
            if not data:
                print('Lost Connection with',self.client_address)
                break
            else:
                print("{}wrote:".format(self.client_address))
                print('Recved:',data)
                self.request.send(data.upper())

if __name__ == '__main__':
    print ( 'MySocketServer is Runing; Host=%s; Port=%s ... ...' % (HOST , PORT) )
    HOST,PORT = '0.0.0.0',50007
    server = socketserver.ThreadingTCPServer((HOST,PORT),MySocketServer)
    server.serve_forever()
