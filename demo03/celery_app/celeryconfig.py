# -*- coding:utf-8 -*-
from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = "redis://127.0.0.1:6379/1"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/2"

#指定时区
CELERY_TIMEZONE = "Asia/Shanghai"

#导入指定的任模块
CELERY_IMPORTS = {
    "celery_app.task1",
    "celery_app.task2",
}

#------下面是配置定时，如果不需要定时就不需要配置------
CELERYBEAT_SCHEDULE = {
    'task1':{
        'task':'celery_app.task1.add',
        'schedule':timedelta(seconds=20),
        'args':(2,8)
    },
    'task2':{
        'task':'celery_app.task2.multiply',
        'schedule':crontab(hour=18,minute=7),
        'args':(3,9)
    }
}
