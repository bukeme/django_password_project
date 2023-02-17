from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Password_Manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=300, null=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    logo = models.CharField(max_length=300)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')
    