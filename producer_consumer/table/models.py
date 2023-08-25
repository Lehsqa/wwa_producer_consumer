from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    task_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    probation = models.BooleanField(default=False)
    position = models.CharField(max_length=100, null=True, default='Developer')

    def __str__(self):
        return self.user.username
