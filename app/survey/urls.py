
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('_icf001/', views._icf001_index, name='_icf001'),#list
    path('_icf001/p2/', views._icf001_p2, name='_icf001_p2'),#list
    path('_icf001/end/', views._icf001_end, name='_icf001_end'),#list
    path('_icf002/', views._icf002_index, name='_icf002'),#list
    ]