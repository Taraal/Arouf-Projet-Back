from django.urls import path

from . import views

app_name='api_users'

urlpatterns = [
    path('get/all/', views.getAllUsers, name='getAllUsers'),
    path('add/', views.insertUser, name='addUser'),
    path('get/', views.getUser, name='getUser'),
    path('auth/', views.authenticate, name='authenticate'),
    path('error/', views.errorTest, name='errorTest'),
]