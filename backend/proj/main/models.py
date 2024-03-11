from django.db import models
from accounts.models import User
# Create your models here.

class ActiveQuerySet(models.QuerySet):
    def is_active(self):
        return self.filter(is_active=True)
    
class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    name=models.CharField(max_length=20)
    age=models.PositiveIntegerField()
    phone=models.PositiveIntegerField()
    email=models.EmailField(max_length=254)
    aadhar=models.PositiveIntegerField()
    street=models.CharField(max_length=30)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    rating=models.IntegerField()
    helper=models.IntegerField()
    def __str__(self):
        return self.name
    


class Helper(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    name=models.CharField(max_length=20)
    age=models.PositiveIntegerField(default=18)
    phone=models.PositiveIntegerField(default=0)
    email=models.EmailField(max_length=254)
    aadhar=models.PositiveIntegerField()
    street=models.CharField(max_length=30)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    rating=models.IntegerField()
    is_active=models.BooleanField(default=False)
    objects=ActiveQuerySet().as_manager()

    def __str__(self):
        return self.name



class Skill(models.Model):
    name = models.CharField(max_length=100)
    rating=models.PositiveIntegerField(default=0)
    helper=models.ForeignKey(Helper,on_delete=models.CASCADE,related_name='skill', default=None)
    def __str__(self):
        return self.name