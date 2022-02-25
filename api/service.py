from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers 
from app.treatment.models import Service
from django.http import Http404
import django_filters

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields =  ['uuid','code','name','list_price']


class ServiceFilter(django_filters.FilterSet):
    code = django_filters.CharFilter(lookup_expr='icontains')
    name = django_filters.CharFilter(lookup_expr='icontains')
    

    class Meta:
        model = Service
        fields = ['name','code',]

    
class ServiceList(ListAPIView):
    queryset = Service.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = ServiceSerializer
    filter_class = ServiceFilter
    
    def get_object(self):
        try:
            return self.queryset.get(patient__uuid = self.kwargs['uuid'])
        except Service.DoesNotExist:
            raise Http404


