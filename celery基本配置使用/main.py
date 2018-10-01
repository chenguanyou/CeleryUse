#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/29 12:18
# @User    : zhunishengrikuaile
# @File    : main.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: py_code
from celery_app.task_1 import add
from celery_app.task_2 import add_2

print('开始执行')
result = add.delay(10, 2)
result_2 = add_2.delay(19, 20)
print(result)
print('结束执行')
print(result.get())
print(result_2.get())