# -*- coding:utf-8 -*-

BROKER_URL = "redis://127.0.0.1:6379/1"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/2"

#指定时区
CELERY_TIMEZONE = "Asia/Shanghai"

#导入指定的任模块
CELERY_IMPORTS = {
    "celery_app.task1",
    "celery_app.task2"
}