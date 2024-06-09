from celery import Celery

celery = Celery('tasks', broker='redis://redis:6379/0')


@celery.task
def add(x, y):
    print('red')
    return x + y

