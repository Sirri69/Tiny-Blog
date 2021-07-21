from django.urls import path
from Documentor import views

urlpatterns = [
    path('', views.index),
    path('check_username', views.check_username),
    path('check_mail', views.check_email),
]