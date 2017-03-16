#!/usr/bin/env python
# encoding: utf-8

"""
@version: Python 2.7
@author: Admin
@license: Apache Licence 
@contact: yang.hu@live.com
@software: PyCharm
@file: mp3Play.py
@time: 2017/2/9 16:49
"""

import time
import pygame
import sys, time

file = r'test.mp3'
pygame.mixer.init()
print("播放音乐")
track = pygame.mixer.music.load(file)

pygame.mixer.music.play()
time.sleep(600)

