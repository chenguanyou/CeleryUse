#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/29 13:29
# @User    : zhunishengrikuaile
# @File    : main.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: py_code
from celery_app.task_1 import name
from celery_app.task_2 import sex
from celery_app.task_3 import age

if __name__ == "__main__":
    name = name.delay('陈书剑')
    sex = sex.delay('男')
    age = age.delay(22)
    print(name)
    print(sex)
    print(age)
    print(name.get())
    print(sex.get())
    print(age.get())