#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/29 12:19
# @User    : zhunishengrikuaile
# @File    : task_1.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: py_code
import time
from celery_app import app

@app.task
def add(x, y):
    time.sleep(4)
    return x + y

