from django.db import models
from datetime import datetime

class User(models.Model):
    name = models.CharField(max_length = 150)
    password = models.CharField(max_length = 20)
    dtTime = models.DateTimeField(default=datetime.now,blank=True)
    localId = models.IntegerField()
     
    
