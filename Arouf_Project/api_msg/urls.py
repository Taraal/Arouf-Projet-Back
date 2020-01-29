from django.urls import path

from . import views

app_name = 'api_msg'

urlpatterns = [
    path('send/', views.send, name='send'),
    path('receive/', views.receive, name='receive')
]