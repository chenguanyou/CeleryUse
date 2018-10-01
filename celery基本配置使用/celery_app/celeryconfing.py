#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/29 12:19
# @User    : zhunishengrikuaile
# @File    : celeryconfing.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: py_code

BROKER_URL = "redis://127.0.0.1:6379/1"

CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/2"

# CELERY_TIMEZONE = 'Asina/Shanghai' # 指定UTC时区

# 加载任务模块
CELERY_IMPORTS = (
    'celery_app.task_1',
    'celery_app.task_2'
)
