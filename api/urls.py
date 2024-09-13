
from django.contrib import admin
from django.urls import include, path

from .views import CarCreate, CarDelete, CarList

urlpatterns = [
    path('', CarList.as_view()),
    path('delete/<int:pk>/', CarDelete.as_view()),
    path('create/', CarCreate.as_view()),
    

]
