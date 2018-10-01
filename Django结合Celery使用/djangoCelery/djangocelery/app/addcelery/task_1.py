#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/29 14:53
# @User    : zhunishengrikuaile
# @File    : task_1.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: djangoCelery
import time
from celery.task import Task


class CourseTask(Task):
    name = 'course-task'

    def run(self, *args, **kwargs):
        print('任务开始')
        time.sleep(10)
        print('args={}, kwargs={}'.format(args, kwargs))
        print('任务结束')
