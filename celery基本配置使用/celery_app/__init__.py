#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/29 12:18
# @User    : zhunishengrikuaile
# @File    : __init__.py.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: py_code
from celery import Celery

app = Celery('demo')

app.config_from_object('celery_app.celeryconfing')  # 通过Celery实例加载配置模块
