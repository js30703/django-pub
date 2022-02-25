
from django.urls import path, re_path, include
from . import views

urlpatterns = [

    path('', views.pay_list, name='payment_list'),#list
    path('<str:pk>/', views.pay_create, name='payment_create'),#detail  
    
    
]