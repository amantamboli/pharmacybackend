# models.py
from django.db import models

class userAdmin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_no = models.CharField(max_length=15)

    def __str__(self):
        return self.name