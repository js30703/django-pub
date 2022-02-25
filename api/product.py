from django.db.models.fields import CharField
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers 
from app.treatment.models import Product, Service, Treatment
from django.http import Http404
import django_filters



class ProductCreateSerializer(serializers.Serializer):
    
    treatment_id = serializers.CharField(write_only=True)
    service_id = serializers.CharField(write_only=True) 
    teeth = serializers.CharField()
    
    quantity = serializers.IntegerField()
    
    price = serializers.SerializerMethodField(read_only=True)
    name = serializers.SerializerMethodField(read_only=True)
    uuid = serializers.CharField(read_only=True)

    def get_name (self,obj):
        return obj.service.name

    def get_price(self, obj):
        return obj.service.list_price
    
    def create(self, validated_data):
        
        return Product.objects.create(
                treatment = Treatment.objects.get(uuid=validated_data['treatment_id']),
                service = Service.objects.get(uuid=validated_data['service_id']),
                teeth = validated_data['teeth'],
                quantity = validated_data['quantity']
        )

    
class ProductCreate(CreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = ProductCreateSerializer
    
    
class ProductDeleteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id',]
    
    
class ProductDelete(DestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = ProductDeleteSerializer
    
    def get_object(self):
        try:
            return self.queryset.get(uuid = self.kwargs['uuid'])
        except Product.DoesNotExist:
            raise Http404
    
   

