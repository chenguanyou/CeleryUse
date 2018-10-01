#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/29 12:50
# @User    : zhunishengrikuaile
# @File    : test.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: py_code
import time
from celery import Celery

broker = "redis://127.0.0.1:6379/1"
backend = "redis://127.0.0.1:6379/2"

app=Celery('test', broker=broker, backend=backend)

@app.task
def test_add(x, y):
    print('执行')
    time.sleep(2)
    return x + y


if __name__ == "__main__":
    print('开始')
    result = test_add.delay(10, 20)
    result_1 = test_add.delay(20, 1)
    print(result.get())
    print(result_1.get())
    print('结束')


