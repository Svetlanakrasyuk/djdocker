from celery import shared_task


@shared_task
def mytask():
    return 'mytask work'

@shared_task
def add(x, y):
    return x + y