import os
from django.core.files.base import ContentFile
from app.payment.create_invoice import create_invoice
from utills.pdf.draw_invoice import draw_invoice
from django.db.models import Prefetch
from app.treatment.models import Treatment, Product

from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers 
from app.payment.models import Payment
from django.http import Http404


   
class PaymentDeleteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = ['id',]
    

    
    
    
class PaymentDelete(DestroyAPIView):
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = PaymentDeleteSerializer
    
    def get_object(self):
        try:
            return self.queryset.get(uuid = self.kwargs['uuid'])
        except Payment.DoesNotExist:
            raise Http404
    
    def perform_destroy(self, payment):
        uuid = payment.treatment.uuid
        payment.delete()
        create_invoice(uuid)