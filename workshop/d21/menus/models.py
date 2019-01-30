from django.db import models

# Create your models here.
class Question(models.Model):
    title=models.CharField(max_length=40)
    
class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    content=models.CharField(max_length=40)
    votes=models.IntegerField()