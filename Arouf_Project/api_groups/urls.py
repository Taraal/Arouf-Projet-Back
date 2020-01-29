from django.urls import path

from . import views

app_name = 'api_groups'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('get/', views.get, name='get'),
    path('add/user/', views.adduser, name='adduser')
]