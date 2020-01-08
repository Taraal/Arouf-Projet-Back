from django.urls import path

from . import views

urlpatterns = [
    path('get/all/', views.getAllUsers, name='getAllUsers'),
    path('add/', views.insertUser, name='insertUser'),
    path('get/', views.getUser, name='getUser'),
    path('auth/', views.authenticate, name='authenticate')
]