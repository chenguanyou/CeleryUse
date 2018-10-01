#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/29 13:30
# @User    : zhunishengrikuaile
# @File    : task_1.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: py_code
import time
from celery_app import app

@app.task
def name(name):
    time.sleep(2)
    return name
