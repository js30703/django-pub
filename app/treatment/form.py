from django.forms import ModelForm, TextInput, DateTimeInput,Select, CheckboxSelectMultiple, NumberInput, Textarea, SelectMultiple,NullBooleanSelect
from .models import Treatment
from .models import Service
from .models import Product
from app.authentication.models import User
from app.patient.models import Patient
from django import forms


class TreatmentForm(ModelForm):
    class Meta:
        model = Treatment
        fields = ('user','treatment_time')
        widgets = {
            'user': Select(attrs={"class": "form-control"}),
            'treatment_time': DateTimeInput(attrs={"placeholder":'ex) 2021-05-28T10:30:00',"class": "form-control", "type":"datetime-local"}),

        }
    
        
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(TreatmentForm, self).__init__(*args, **kwargs)
        self.fields["treatment_time"].input_formats = ['%Y-%m-%dT%H:%M']
        self.fields["user"].queryset = User.objects.filter(type__in=['Doctor','Supervisor',])
        

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('teeth','service','quantity')
        widgets = {
            'teeth': TextInput(attrs={"class": "form-control"}),
            'service': Select(attrs={"class": "form-control"}),
            'quantity': NumberInput(attrs={"class": "form-control"}),

        }
    
        
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["service"].queryset = Service.objects.all()


class UploadFileForm(forms.Form):
    file = forms.FileField()



class TreatmentUpdateForm(ModelForm):
    class Meta:
        model = Treatment
        fields = ('next_treatement','diagnosis',)
        widgets = {
            'diagnosis': Textarea(attrs={"class": "form-control", "rows":"5", "placeholder":"Less than 250 letters"}),
            'next_treatement': Textarea(attrs={"class": "form-control", "rows":"5", "placeholder":"Less than 250 letters"}),
        }
    
        
    def __init__(self, *args, **kwargs):
        super(TreatmentUpdateForm, self).__init__(*args, **kwargs)
        
        