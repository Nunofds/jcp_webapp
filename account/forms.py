from captcha.fields import ReCaptchaField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class InscriptionForm(UserCreationForm, ReCaptchaField):
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'validate', }))

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Nom d\'utilisateur ou email'}
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Mot de passe'}
    ))
