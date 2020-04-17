
# -*- coding:utf-8 -*-

from celery import Celery

app = Celery("demo")
# 通过celery实例加载配置模块
app.config_from_object("celery_app.celeryconfig")


# import time
#
# broker = "redis://127.0.0.1:6379/1"
# backend = "redis://127.0.0.1:6379/2"
# app = Celery("my_task",broker=broker,backend=backend)
#
# @app.task
# def add(x,y):
#     print("runfunc....")
#     time.sleep(20)
#     return x+y