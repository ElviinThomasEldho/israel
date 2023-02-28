from django.forms import ModelForm
from .models import *
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = '__all__'

        widgets = {
            'about' : forms.Textarea(),
            'email' : forms.EmailInput(),
            'mobile' : forms.TextInput(),
            'address' : forms.Textarea(),
        }

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput(),
            'desc' : forms.Textarea(),
        }

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput(),
            'occupation' : forms.TextInput(),
            'desc' : forms.TextInput(),
            'dateOfTravel' : DateInput(),
            'title' : forms.TextInput(),
            'desc' : forms.Textarea(),
        }