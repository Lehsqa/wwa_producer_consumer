import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'producer_consumer.settings')

app = Celery('producer_consumer')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'add_order_minutely': {
        'task': 'table.tasks.add_order',
        'schedule': 60.0
    }
}

app.autodiscover_tasks()
