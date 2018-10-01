#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/29 13:30
# @User    : zhunishengrikuaile
# @File    : celeryconfing.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: py_code
from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = "redis://127.0.0.1:6379/1"

CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/2"

CELERY_TIMEZONE = 'Asia/Shanghai'

# 配置任务模块
CELERY_IMPORTS = (
    'celery_app.task_1',
    'celery_app.task_2',
    'celery_app.task_3'
)

# 配置定时任务
# 定时任务执行命令：celery beat -A 任务地址 -l INFO
CELERYBEAT_SCHEDULE = {
    # 任务1， 每10秒执行一次
    'task1':{
        'task':'celery_app.task_1.name',
        'schedule': timedelta(seconds=10),
        'args': ('陈书剑',)
    },
    # 任务2， 每天执行14点20执行一次
    'task2':{
        'task':'celery_app.task_2.sex',
        'schedule': crontab(hour=14, minute=20),
        'args': ('男',)
    }
}
