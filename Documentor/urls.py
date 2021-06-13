from django.urls import path
from Documentor import views

urlpatterns = [
    path('', views.index, name='index'),
]