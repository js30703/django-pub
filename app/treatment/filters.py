import django_filters as filter
from .models import Service, Treatment
from django.forms import ModelForm, TextInput, DateInput,Select, CheckboxSelectMultiple


class TreatmentFilter(filter.FilterSet):
    patient__name = filter.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Service
        fields = ['patient__name', ]

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
            super(TreatmentFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
            self.filters['patient__name'].field.widget.attrs.update({'class': 'form-control'})
            





class ServiceFilter(filter.FilterSet):
    code = filter.CharFilter(lookup_expr='icontains')
    name = filter.CharFilter(lookup_expr='icontains')
    
    
    class Meta:
        model = Service
        fields = ['code', 'name']

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
            super(ServiceFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
            self.filters['name'].field.widget.attrs.update({'class': 'form-control'})
            self.filters['code'].field.widget.attrs.update({'class': 'form-control'})
            