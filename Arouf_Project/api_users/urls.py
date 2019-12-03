from django.urls import path

from . import views

urlpatterns = [
    path('', views.getAllUsers, name='getAllUsers'),
    path('user-add/', views.insertUser, name='insertUser'),
]