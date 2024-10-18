
from django.contrib import admin
from django.urls import include, path

from .views import AplicationsList

urlpatterns = [
    path('aplications/', AplicationsList.as_view(), name="all_aplications"),
        
]
