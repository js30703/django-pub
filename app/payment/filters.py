import django_filters as filter
from .models import Payment
from django.forms import ModelForm, TextInput, DateInput,Select, CheckboxSelectMultiple


class PaymentFilter(filter.FilterSet):
    treatment__patient__name = filter.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Payment
        fields = ['treatment__patient__name', ]

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
            super(PaymentFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
            self.filters['treatment__patient__name'].field.widget.attrs.update({'class': 'form-control'})
            
