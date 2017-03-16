# -*- coding: utf-8 -*-
#
# Copyright (C) 2010-2016 PPMessage.
# Yuan Wanshang, wanshang.yuan@yvertical.com.
# Guijin Ding, dingguijin@gmail.com.
#
# All rights are reserved.
#

from ppmessage.core.constant import REDIS_HOST
from ppmessage.core.constant import REDIS_PORT
from ppmessage.core.constant import PP_WEB_SERVICE

from ppmessage.core.singleton import singleton
from ppmessage.core.main import AbstractWebService

from ppmessage.core.downloadhandler import DownloadHandler

import redis
from tornado.web import Application

@singleton
class DownloadDelegate():
    def __init__(self, app):
        return
    def run_periodic(self):
        return

class DownloadWebService(AbstractWebService):

    @classmethod
    def name(cls):
        return PP_WEB_SERVICE.PPDOWNLOAD

    @classmethod
    def get_handlers(cls):
        return [("/ppdownload/([^\/]+)?$", DownloadHandler, {"path": "/"})]

    @classmethod
    def get_delegate(cls, app):
        return DownloadDelegate(app)
    
    
