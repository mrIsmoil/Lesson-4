from django.db import models
from multiselectfield import MultiSelectField
# from user.models import User
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
   # user= models.ForeignKey(User, on_delete=models.CASCADE)
   name= models.CharField( max_length=50)
   model= models.CharField(max_length=100)
   color= MultiSelectField(choices=COLORS)
   description = models.TextField()
   created = models.DateTimeField(  auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)

class User(models.Model):
   name = models.CharField(max_length=40)
   email = models.EmailField()
   username = models.CharField(max_length=40)

   def __str__(self):
      return self.name

class Message(models.Model):
   sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
   receiver_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
   text = models.TextField()
   date = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return f"Message from {self.sender} to {self.receiver}"