# -*- coding: utf-8 -*-
#
# Copyright (C) 2010-2016 PPMessage.
# Guijin Ding, dingguijin@gmail.com.
# All rights are reserved.
#

from .wshandler import WSHandler

from ppmessage.core.constant import PCSOCKET_SRV

from ppmessage.core.constant import REDIS_ACK_NOTIFICATION_KEY
from ppmessage.core.constant import REDIS_PUSH_NOTIFICATION_KEY
from ppmessage.core.constant import REDIS_SEND_NOTIFICATION_KEY

from ppmessage.core.constant import DIS_WHAT
from ppmessage.core.constant import PP_WEB_SERVICE
from ppmessage.core.constant import DATETIME_FORMAT

from ppmessage.core.singleton import singleton
from ppmessage.core.main import AbstractWebService

from ppmessage.core.utils.getipaddress import get_ip_address
from ppmessage.core.utils.datetimestring import now_to_string

from ppmessage.db.models import AppInfo
from ppmessage.db.models import DeviceInfo
from ppmessage.db.models import ConversationUserData

from ppmessage.dispatcher.policy import BroadcastPolicy

from .error import DIS_ERR

import tornado.options
from tornado.options import options
from tornado.web import Application
from tornado.ioloop import PeriodicCallback

import datetime
import logging
import redis
import uuid
import time
import json
import copy


@singleton
class PCSocketDelegate():
    def __init__(self, app):
        self.app = app
        self.redis = app.redis
        self.sockets = {}
        return
        
    def device_online(self, _device_uuid, _is_online=True):
        _row = DeviceInfo(uuid=_device_uuid, device_is_online=_is_online)
        _row.async_update(self.redis)
        _row.update_redis_keys(self.redis)
        return
        
    def send_send(self, _device_uuid, _body):
        _body["pcsocket"] = {
            "device_uuid": _device_uuid
        }
        _key = REDIS_SEND_NOTIFICATION_KEY
        self.redis.rpush(_key, json.dumps(_body))
        return
    
    def save_extra(self, _user_uuid, _extra_data):
        return
    
    def ack_loop(self):
        """
        every 100ms check ack notification
        """
        key = REDIS_ACK_NOTIFICATION_KEY
        while True:
            noti = self.redis.lpop(key)
            if noti == None:
                # no message
                return
            body = json.loads(noti)
            ws = self.sockets.get(body.get("device_uuid"))
            if ws == None:
                logging.error("No WS to handle ack body: %s" % body) 
                continue
            ws.send_ack(body)
        return

    def push_loop(self):
        """
        every 50ms check push notification
        """
        
        key = REDIS_PUSH_NOTIFICATION_KEY
        
        while True:
            noti = self.redis.lpop(key)
            if noti == None:
                return

            body = json.loads(noti)
            logging.info("WS will send: %s" % body)
            pcsocket = body.get("pcsocket") 
            if pcsocket == None:
                logging.error("no pcsocket in push: %s" % (body))
                continue
            device_uuid = pcsocket.get("device_uuid")
            ws = self.sockets.get(device_uuid)
            if ws == None:
                logging.error("No WS handle push: %s" % body)
                continue
            ws.send_msg(body["body"])

        return

    def run_periodic(self):
        tornado.options.parse_command_line()

        # set the periodic check ack every 50 ms
        PeriodicCallback(self.ack_loop, 50).start()

        # set the periodic check push every 50 ms
        PeriodicCallback(self.push_loop, 50).start()
        return

class PCSocketWebService(AbstractWebService):
    @classmethod
    def name(cls):
        return PP_WEB_SERVICE.PCSOCKET

    @classmethod
    def get_handlers(cls):
        return [("/"+PCSOCKET_SRV.WS, WSHandler)]

    @classmethod
    def get_delegate(cls, app):
        return PCSocketDelegate(app)


