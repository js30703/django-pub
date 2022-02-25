from django.forms import ModelForm, TextInput, DateTimeInput,Select, CheckboxSelectMultiple, NumberInput, Textarea, SelectMultiple,CheckboxInput,RadioSelect,DateInput, TimeInput
from app.treatment.models import Treatment
from app.authentication.models import User
from .models import ICF001, IFC001_2, ICF002
from django import forms


class ICF001Form(ModelForm):
    class Meta:
        model = ICF001
        fields = ('ga_id','q1','q2','q7','q3','q4','q5','q6','q6_other',)
        widgets = {
            'ga_id': TextInput(attrs={"class": "form-control d-none"}),
            'q1': TextInput(attrs={"class": "form-control"}),
            'q2': TextInput(attrs={"class": "form-control"}),
            'q7': TextInput(attrs={"class": "form-control"}),
            'q3': TextInput(attrs={"class": "form-control"}),
            'q4': TextInput(attrs={"class": "form-control"}),
            'q5': TextInput(attrs={"class": "form-control"}),
            'q6': SelectMultiple(attrs={"class": "form-control h-10"}),
            'q6_other': TextInput(attrs={"class": "form-control"}),
        }
    
        
    def __init__(self, *args, **kwargs):
        super(ICF001Form, self).__init__(*args, **kwargs)
        



class IFC001_2Form(ModelForm):
    class Meta:
        model = IFC001_2
        fields =  ('q1','q2','q2_other','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17',)
        widgets = {
            
            'q1': TextInput(attrs={"class": "form-control"}),
            'q2': Select(attrs={"class": "form-control"}),
            'q2_other': TextInput(attrs={"class": "form-control"}),
            'q3': Textarea(attrs={"class": "form-control"}),
            'q4': Select(attrs={"class": "form-control"}),
            'q5': Select(attrs={"class": "form-control"}),
            'q6': Select(attrs={"class": "form-control h-10"}),
            'q7': Select(attrs={"class": "form-control"}),
            'q8': Select(attrs={"class": "form-control"}),
            'q9': Select(attrs={"class": "form-control"}),
            'q10': Select(attrs={"class": "form-control"}),
            'q11': Select(attrs={"class": "form-control"}),
            'q12': Select(attrs={"class": "form-control"}),
            'q13': Select(attrs={"class": "form-control"}),
            'q14': DateTimeInput(attrs={"class": "form-control", "type":"date"}),
            'q15': Select(attrs={"class": "form-control"}),
            'q16': Select(attrs={"class": "form-control"}),
            'q17': CheckboxSelectMultiple(attrs={"class": "d-blcok","style":"font-size: 2rem;"}),
            

        }
    
        
    def __init__(self, *args, **kwargs):
        super(IFC001_2Form, self).__init__(*args, **kwargs)
        


class ICF002Form(ModelForm):
    class Meta:
        model = ICF002
        fields = ('name', 'phone', 'service','date', 'time')
        widgets = {
            'name': TextInput(attrs={"class": "form-control"}),
            'phone': TextInput(attrs={"class": "form-control"}),    
            'service': Select(attrs={"class": "form-control"}),        
            'date': DateInput(attrs={"class": "form-control","type":"date"}),    
            'time': TimeInput(attrs={"class": "form-control","type":"time"}),    
        }