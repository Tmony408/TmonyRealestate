from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    purchase_index = models.IntegerField()
    listing= models.CharField(max_length=200)
    listing_id = models.IntegerField()
    realtor_name= models.CharField(max_length=200,)
    name= models.CharField(max_length=200)
    phone = models.CharField(max_length=40) 
    message = models.TextField(blank=True)
    email= models.CharField(max_length= 50)
    user_id = models.IntegerField(blank=True)
    purchase_date= models.DateTimeField(default=datetime.now, blank= True)
    def __str__(self):
        return self.name