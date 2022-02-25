import django_filters as filter
from .models import Patient
from django.forms import ModelForm, TextInput, DateInput,Select, CheckboxSelectMultiple

class PatientFilter(filter.FilterSet):
    name = filter.CharFilter(lookup_expr='icontains')
    birth_date = filter.DateTimeFilter(
        widget = DateInput(attrs={'class': 'form-control', "type":"date"})
        )
    
    class Meta:
        model = Patient
        fields = ['name', 'birth_date']

    def __init__(self, data=None, queryset=None, request=None, prefix=None):
            super(PatientFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
            self.filters['name'].field.widget.attrs.update({'class': 'form-control'})
            