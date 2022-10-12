from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from captcha.fields import ReCaptchaField
from django import forms


# REGISTER
class InscriptionForm(UserCreationForm, ReCaptchaField):
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
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']

    # email unique, return error if the email exists in BDD
    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_count = User.objects.filter(email=email).count()
        if user_count > 0:
            raise forms.ValidationError('Un compte avec ce email existe déjà.')
        return email

    # fonction for save form with some personalisation for email
    # def save(self, commit=True):
    #     user = super(InscriptionForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user


# LOGIN
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
            'placeholder': 'Mot de passe'}),
    )
