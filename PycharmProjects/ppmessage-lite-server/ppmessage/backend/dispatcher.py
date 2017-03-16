# -*- coding: utf-8 -*-
#
# Copyright (C) 2010-2016 PPMessage.
# Guijin Ding, dingguijin@gmail.com
# All rights reserved
#
# backend/dispatcher.py 
# The entry form Dispatcher service
#
#

from ppmessage.core.constant import REDIS_HOST
from ppmessage.core.constant import REDIS_PORT
from ppmessage.core.constant import PP_WEB_SERVICE
from ppmessage.core.constant import REDIS_DISPATCHER_NOTIFICATION_KEY

from ppmessage.dispatcher.task import TaskHandler

from ppmessage.core.singleton import singleton
from ppmessage.core.main import AbstractWebService

import tornado.web
import tornado.ioloop
import tornado.options

import json
import redis
import logging
import datetime

@singleton
class DispatcherDelegate():
    def __init__(self, app):
        self.redis = app.redis
        self.task_handler = TaskHandler(self)
        return

    def run_periodic(self):
        # every 20ms check dispatcher task
        tornado.ioloop.PeriodicCallback(self.task_loop, 20).start()
        return

    def task_loop(self):
        """
        every 20ms check task notification
        """
        key = REDIS_DISPATCHER_NOTIFICATION_KEY
        while True:
            noti = self.redis.lpop(key)
            if noti == None:
                # no message
                return
            body = json.loads(noti)
            self.task_handler.task(body)
        return
    
class DispatcherWebService(AbstractWebService):

    @classmethod
    def name(cls):
        return PP_WEB_SERVICE.DISPATCHER

    @classmethod
    def get_handlers(cls):
        return []

    @classmethod
    def get_delegate(cls, app):
        return DispatcherDelegate(app)

