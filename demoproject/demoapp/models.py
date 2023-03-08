from django.db import models
from unicodedata import name

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length = 30)
    cousine = models.CharField(max_length = 10)
    price = models.IntegerField()

    def __str__(self):
       return self.name + " " + self.cousine    
    
class Logger(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    time_log = models.TimeField()

class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('Phone Number', max_length=300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300,blank=True)
    
    def __str__(self):
        return self.name