from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('signup/confirm_email', views.register),
    path('signup', views.signup),
    path('login', views.login_user),
    path('profile', views.profile),
    path('confirm_email/<str:enc>', views.confirm_email),
    path('reset_password/<str:enc>', views.password_reset),
    path('reset_password/', views.password_reset),
    # path('')
    path('home', views.home)
]