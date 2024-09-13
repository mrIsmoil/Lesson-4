from django.contrib import admin

from .models import Car, User, Message

admin.site.register(Car)
admin.site.register(User)
admin.site.register(Message)