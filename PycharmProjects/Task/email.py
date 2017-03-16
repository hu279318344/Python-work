#!/usr/bin/env python
# encoding: utf-8

"""
@version: Python 3.6
@author: Admin
@license: Apache Licence 
@contact: yang.hu@live.com
@software: PyCharm
@file: email.py
@time: 2017/2/20 15:57
"""

import smtplib
import email


msg = email.message_from_bytes()
msg['from'] = "279318344@qq.com"
msg['to'] = '279318344@qq.com'
msg['subject'] = 'test'
content = '''''
    你好，
            这是一封自动发送的邮件。

        www.ustchacker.com
'''
txt = email.mime.text.MIMEText ( content )
msg.attach ( txt )

smtp = smtplib
smtp = smtplib.SMTP ( )
smtp.connect ( 'smtp.qq.com', '25' )
smtp.login ( '279318344@qq.com', 'hujie772**' )
smtp.sendmail ( '279318344@qq.com', '279318344@qq.com', str ( msg ) )
smtp.quit ( )