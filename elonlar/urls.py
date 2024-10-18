
from django.contrib import admin
from django.urls import include, path

from .views import Joblist

urlpatterns = [
        path('', Joblist.as_view(), name="all_jobs"),
        
]
