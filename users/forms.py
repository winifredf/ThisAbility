from django import forms
from .models import Employer

class EmployerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['name', 'address', 'phone', 'email', 'username', 'password', 'user']
        widgets = {
            'password': forms.PasswordInput()
        }
