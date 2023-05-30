from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostModel(models.Model):
    tittle = models.CharField(max_length=50)
    body = models.TextField(max_length=900)
    author = models.ForeignKey(User,max_length=12,on_delete=models.SET_NULL,null=True)



    def __str__(self):
        return self.tittle