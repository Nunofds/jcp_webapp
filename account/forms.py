from captcha.fields import ReCaptchaField
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.core.validators import RegexValidator


class InscriptionForm(UserCreationForm, ReCaptchaField):
    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'validate', })
    )
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'validate'}),
        validators=[RegexValidator(
            regex="^[a-zA-Z ]*$",
            message='Veuillez entrer un nom valide! Pas de chiffres ni caractères speciaux.',
        )],
    )

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'username', 'email', 'password1', 'password2']

    # fonction for save form with some personalisation for email
    def save(self, commit=True):
        user = super(InscriptionForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Nom d\'utilisateur ou email'}),
                               )

    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Mot de passe'}
    ))
