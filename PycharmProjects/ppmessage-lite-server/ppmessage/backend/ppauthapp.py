#
# Copyright (C) 2010-2016 PPMessage.
# Guijin Ding, dingguijin@gmail.com.
# All rights reserved.
#
# backend/ppauthapp.py
#

from ppmessage.ppauth.authhandler import AuthHandler
from ppmessage.ppauth.tokenhandler import TokenHandler

from ppmessage.core.constant import PP_WEB_SERVICE
from ppmessage.core.main import AbstractWebService
from ppmessage.core.singleton import singleton

import os
import redis
import tornado.web

@singleton
class PPAuthDelegate():
    def __init__(self, app):
        return
    def run_periodic(self):
        return

class PPAuthWebService(AbstractWebService):

    @classmethod
    def name(cls):
        return PP_WEB_SERVICE.PPAUTH

    @classmethod
    def get_handlers(cls):
        _a_settings = {
            "path": os.path.join(os.path.dirname(__file__), "../resource/assets/ppcom/static"),
        }
        
        handlers = [
            ("/auth/?.*", AuthHandler),
            ("/token/?.*", TokenHandler),
            ("/static/(.*)", tornado.web.StaticFileHandler, _a_settings)
        ]

        return handlers

    @classmethod
    def get_delegate(cls, app):
        return PPAuthDelegate(app)
    
