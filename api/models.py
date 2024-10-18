from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField

COLORS=[
   ('blck', 'Black'),
   ('wht', 'White'),
   ('bl', 'Blue'),
   ('rd', 'Red'),
   ('yllw', 'Yellow'),
   ('gry', 'Grey'),
   ('grn', 'Green'),
]

class Car(models.Model):
   
   name= models.CharField( max_length=50)
   model= models.CharField(max_length=100, verbose_name='model')
   color= MultiSelectField(choices=COLORS, verbose_name='rang')
   description = models.TextField(verbose_name='tavsif')
   created = models.DateTimeField(  auto_now_add=True, verbose_name='yaratilgan')
   updated = models.DateTimeField(auto_now=True, verbose_name='yangilangan')
class CustomUser(AbstractUser):
   name = models.CharField(max_length=40, verbose_name='foydalanuvchi')
   email = models.EmailField() 
   groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to.',
    )
   user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
   
   def __str__(self):
      return self.name

class Message(models.Model):
   sender_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
   receiver_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')
   text = models.TextField(verbose_name='matn')
   date = models.DateTimeField(auto_now_add=True, verbose_name='sana')

   def __str__(self):
      return f"Message from {self.sender_id} to {self.receiver_id}"