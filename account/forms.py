from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
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


# PASSWORD CHANGE
class SetNewPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']


# PASSWORD RESET
class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)
