from django.db import models
from django.contrib.auth.models import AbstractUser

class Userlar(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')
    profile_image = models.ImageField(upload_to='profile_images/')
    is_company = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    manager = models.BooleanField(default=False)
    worker = models.BooleanField(default=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.last_name
