from django.db.models import fields
from rest_framework import permissions
from rest_framework.generics import ListAPIView,UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers 
from app.patient.models import Odontogram, Patient
from django.http import Http404


class OdontogramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Odontogram
        fields = "__all__"



    
class OdontogramUpdate(UpdateAPIView):
    queryset = Odontogram.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = OdontogramSerializer
    
    def get_object(self):
        try:
            return self.queryset.get(patient__uuid = self.kwargs['uuid'])
        except Patient.DoesNotExist:
            raise Http404


