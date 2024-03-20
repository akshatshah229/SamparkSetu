from django import forms
from .models import *

class FormViewsModel(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'listings': forms.RadioSelect(attrs={'class':'form-control'}),
            'apartment': forms.RadioSelect(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'message': forms.Textarea(attrs={'class':'form-control'}),
        }