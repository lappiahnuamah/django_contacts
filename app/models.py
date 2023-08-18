from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=50)
    email =  models.EmailField(max_length=254)
    phone = models.IntegerField()
    info = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ))
    date = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
    