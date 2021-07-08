from django.urls import path
from Documentor import views

urlpatterns = [
    path('', views.index),
    path('check_username', views.check_username)
]