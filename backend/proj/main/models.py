from django.db import models

# Create your models here.

class ActiveQuerySet(models.QuerySet):
    def is_active(self):
        return self.filter(is_active=True)
    
class Customer(models.Model):
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
    
class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Helper(models.Model):
    name=models.CharField(max_length=20)
    age=models.PositiveIntegerField()
    phone=models.PositiveIntegerField()
    email=models.EmailField(max_length=254)
    aadhar=models.PositiveIntegerField()
    street=models.CharField(max_length=30)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    rating=models.IntegerField()
    skills=models.ManyToManyField(Skill)
    is_active=models.BooleanField(default=False)
    objects=ActiveQuerySet().as_manager()

    def __str__(self):
        return self.name
