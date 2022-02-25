from django.forms import ModelForm, TextInput, DateTimeInput,Select, CheckboxSelectMultiple, NumberInput, Textarea, SelectMultiple,NullBooleanSelect
from .models import Payment
from app.authentication.models import User
from app.patient.models import Patient
from django import forms


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ('pay_method','paid_amount')
        widgets = {
            'pay_method': Select(attrs={"class": "form-control"}),
            'paid_amount': NumberInput(attrs={"class": "form-control d-none" , "lang":"en"}),
        }
    
        
    def __init__(self, *args, **kwargs):
        
        super(PaymentForm, self).__init__(*args, **kwargs)
        
