from celery_app import task1
from celery_app import task2

if __name__=="__main__":
    print("start.....")
    # task1.add.apply_async(2,3)
    result = task1.add.delay(2,3)   #这种方式跟上面一样，上面那种可以设定比较多
    task2.multiply.delay(5,6)
    print("end.....")
    print(result)
    # 67f62dd4-99e6-4eb2-8e72-e21562095522
    # from celery.result import AsyncResult
    # res = AsyncResult("67f62dd4-99e6-4eb2-8e72-e21562095522")  # 参数为task id
    # print(res.result)
