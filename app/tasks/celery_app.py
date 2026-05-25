from celery import Celery

def create_celery(app_name=__name__):
    celery = Celery(app_name, broker="redis://redis:6379/0", backend='redis://redis:6379/0')
    return celery 

celery = create_celery()