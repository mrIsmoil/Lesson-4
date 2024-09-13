from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    email = models.EmailField(("email address"), unique=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email
