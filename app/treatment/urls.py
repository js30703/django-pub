
from django.urls import path, re_path, include
from app.treatment import views

urlpatterns = [
    path('', views.list, name='treatment_list'),#list
    path('create/<str:userpk>/', views.create, name='treatment_create'),
    
    path('<str:pk>/', views.detail, name='treatment_detail'),
    
    
    
]