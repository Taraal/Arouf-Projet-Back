from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.add, name='add'),
    path('get/', views.get, name='get'),
    path('add/user/', views.adduser, name='adduser')
]