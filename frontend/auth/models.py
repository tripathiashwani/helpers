from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(maxlen=20)
    age=models.PositiveIntegerField()


class Helper(models.Model):
    name=models.CharField(maxlen=20)
    skill=models.CharField(maxlen=20)
