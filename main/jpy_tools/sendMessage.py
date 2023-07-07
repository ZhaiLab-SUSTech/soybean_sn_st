#!/usr/bin/env python
# -*- coding: utf-8 -*
'''
@Author: liuzj
@Date: 2020-05-09 09:53:11
@LastEditors: liuzj
@LastEditTime: 2020-07-01 16:04:29
@Description: 用来发通知
@FilePath: /liuzj/softwares/python_scripts/sendMessageScript/jpy_sendMessage.py
'''
import requests
import random

def sendMessage(title='empty', content='empty'):
    if (title == 'empty') & (content == 'empty'):
        title += str(random.randint(0, 10000))
        content += str(random.randint(0, 10000))

    api = "https://sc.ftqq.com/SCU97112Tfbdc2547f36c3f5ec63c9e02ed77177d5eb6089893e5e.send"
    data={'text':title,'desp':content}
    requests.post(api,data=data)
