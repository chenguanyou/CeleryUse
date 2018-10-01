#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/29 14:49
# @User    : zhunishengrikuaile
# @File    : celeryconfig.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: djangoCelery
'''
django-celery配置文件
'''
import djcelery

djcelery.setup_loader()

# 防止任务过多时候照成混乱
CELERY_QUEUES = {
    'beat_tasks': {
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks'
    },
    'work_queue': {
        'exchange': 'work_queue',
        'exchange_type': 'direct',
        'binding_key': 'work_queue'
    }
}

CELERY_DEFAULT_QUEUE = 'work_queue'

# 配置任务模块
CELERY_IMPORTS = {
    'app.addcelery.task_1'
}

# 非常重要，有些情况下可以防止死锁
CELERYD_FORCE_EXECV = True

# 设置并发的worker数, 一般根据cpu的数量进行设置
CELERYD_CONCURRENCY = 4

# 如果运行失败了可以尝试
CELERY_ACKS_LATE = True

# 非常重要，设置每个worker执行100次任务就会销毁，这样可以防止内存泄露
CELERYD_MAX_TASKS_PER_CHILD = 100

# 设置单个任务的超时时间
CELERYD_TASK_TIME_LIMIT = 12 * 30

# 创建定时任务
from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'course-task',
        'schedule': timedelta(seconds=10),
        'options': {
            'queue': 'beat_tasks'
        }
    }
}
