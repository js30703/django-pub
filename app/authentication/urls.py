# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from .views import login_view, register_user, change_password
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(next_page='login/'), name="logout"),
    path("password_change/", change_password, name="change_password"),
    path("robots.txt", views.robots, name='home'),
    path('', views.index, name='home'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]
