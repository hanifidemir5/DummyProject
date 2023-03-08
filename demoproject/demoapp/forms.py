from django import forms
from .models import Logger

class LoginForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__' 