from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField

# Create your models here.
class User(models.Model):
    user = OneToOneField(User,on_delete=models.CASCADE)