#!/usr/bin/env python
# encoding: utf-8

import os
version = 0.1
author = 'yanghu'
last_modify = '2017-07-23'

def mem_usage():
    cmd = os.popen('free -m').readlines()
    print(cmd)

if __name__ == '__main__':
    print('Can only be called bu other program')
else:
    mem_usage()

