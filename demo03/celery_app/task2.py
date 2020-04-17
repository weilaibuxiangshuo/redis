# -*- coding:utf-8 -*-

import time
from celery_app import app

@app.task
def multiply(x,y):
    print("runfunc2....")
    time.sleep(10)
    return x*y
