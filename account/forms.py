from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class inscriptionForm(UserCreationForm):
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'validate', }))

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
