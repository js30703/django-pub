from django.urls import path, include
from .odont import OdontogramUpdate
from .service import ServiceList
from .product import ProductCreate, ProductDelete
from .payment import PaymentDelete

urlpatterns = [
    # path('', include('app.user.urls')),
    # path('', include('app.verifier.urls')),
    
    path('service/', ServiceList.as_view()),
    
    path('odont/<str:uuid>/', OdontogramUpdate.as_view()),
    
    path('product/', ProductCreate.as_view()),
    path('product/<str:uuid>/', ProductDelete.as_view()),
    
    path('payment/<str:id>/', PaymentDelete.as_view()),
]
