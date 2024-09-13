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

