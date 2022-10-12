from django.core.validators import RegexValidator
from account.forms import InscriptionForm
from django import forms


class Update_profile(InscriptionForm):
    username = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'validate'}),
    )

    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'validate'}),
        validators=[RegexValidator(
            regex="^[a-zA-Z ]*$",
            message='Veuillez entrer un nom valide! Pas de chiffres ni caractères speciaux.',
        )],
    )

    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={'class': 'validate', }),
        validators=[RegexValidator(
            regex="^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+",
            message='Veuillez entrer un nom valide! Pas de chiffres ni caractères speciaux.',
        )],
    )

    password1 = forms.CharField(
        required=False,
        widget=forms.EmailInput(
            attrs={'class': 'validate', }),
    )

    password2 = forms.CharField(
        required=False,
        widget=forms.EmailInput(
            attrs={'class': 'validate', }),
    )
