from django.urls import path

from . import views

urlpatterns = [
    path('users/get/all/', views.getAllUsers, name='getAllUsers'),
    path('users/add/', views.insertUser, name='insertUser'),
    path('users/get/', views.getUser, name='getUser'),
    path('auth/', views.authenticate, name='authenticate')
]