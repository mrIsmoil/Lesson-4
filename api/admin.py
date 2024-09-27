from django.contrib import admin

from .models import Car, CustomUser, Message

admin.site.register(Car)
admin.site.register(CustomUser)
admin.site.register(Message)