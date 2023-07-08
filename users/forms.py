from django import forms
from .models import Employer

class EmployerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['name', 'address', 'phone', 'email', 'username', 'password', 'user']
        widgets = {
            'password': forms.PasswordInput()
        }

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))