from django.urls import path

from . import views

urlpatterns = [
    path('users/get/all/', views.getAllUsers, name='getAllUsers'),
    path('users/add/', views.insertUser, name='insertUser'),
]