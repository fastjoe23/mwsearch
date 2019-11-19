from django import forms
from .models import MWRequest

class NewMWRequestForm(forms.ModelForm):
    
    class Meta:
        model = MWRequest
        fields = ['postcode', 'birth_date']
