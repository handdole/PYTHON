from django.db import models

# Create your models here.
class Memberlist(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    pw = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    addr = models.CharField(max_length=100)