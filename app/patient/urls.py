
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.list, name='patient_list'),#list
    path('create/', views.create, name='patient_create'),#create
    path('<str:pk>/', views.detail, name='patient_detail'), #retrieve
    #update
    #delete
    ]