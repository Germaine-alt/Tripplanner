# myapp/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    badge_number = forms.CharField(max_length=50, required=True)
    bus_routes = forms.CharField(max_length=200, required=True)
    company_name = forms.CharField(max_length=100, required=True)
    years_experience = forms.IntegerField(required=True)
    bus_type = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'badge_number', 'bus_routes', 'company_name', 'years_experience', 'bus_type']



class RegisterClientForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
