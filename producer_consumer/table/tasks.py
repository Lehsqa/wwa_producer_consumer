import random

from .models import Order
from django.contrib.auth.models import User
from celery import shared_task


@shared_task
def add_order():
    name_id = random.randint(0, 32768)
    employee = User.objects.order_by('?').first()
    Order.objects.create(name=f"Task {name_id}", description=f"Description to Task {name_id}", employee=employee)
    return f"Adding Task {name_id} is done"
