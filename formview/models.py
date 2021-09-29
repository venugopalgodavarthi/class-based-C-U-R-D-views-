
from django.db import models
from django.urls import reverse

# Create your models here.


class empmodel(models.Model):
    name= models.CharField(max_length=30)
    email= models.EmailField(max_length=30)
    sal= models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('listview')
'''
    def get_absolute_url(self):
        return reverse('listview')
'''