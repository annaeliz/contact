from django.db import models
from django.db import models
class contact(models.Model):
    name=models.CharField(max_length=20,blank=True)
    phone=models.CharField(max_length=12,blank=True)


    
