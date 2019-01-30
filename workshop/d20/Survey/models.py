from django.db import models

# Create your models here.
class Quest(models.Model):
    content = models.CharField(max_length=40)
    votes = models.IntegerField()
 
class surv(models.Model):
    title = models.CharField(max_length=40)
    content1 = models.CharField(max_length=40)
    content2 = models.CharField(max_length=40)
    content3 = models.CharField(max_length=40)