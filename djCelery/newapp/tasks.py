import time
from celery import shared_task


@shared_task
def tp1(queue="celery"):
    time.sleep(15)
    return "tp1"


@shared_task
def tp2(queue="celery:1"):
    time.sleep(12)
    return "tp2"


@shared_task
def tp3(queue="celery:2"):
    time.sleep(5)
    return "tp3"


@shared_task
def tp4(queue="celery:3"):
    time.sleep(3)
    return "tp4"
