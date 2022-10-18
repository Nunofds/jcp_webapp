from django import forms
from django.core.validators import RegexValidator
from .models import Contact


class ContactForm(forms.Form):
    class Meta:
        model: Contact

    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Votre nom complet',
            'type': 'text'}),
        validators=[RegexValidator(
            regex="^[a-zA-Z ]*$",
            message='Veuillez entrer un nom valide! Pas de chiffres ni caractères speciaux.',
        )],
    )

    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Votre email'}),
        validators=[RegexValidator(
            regex="^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+",
        )],
    )

    phone = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Votre telephone'}),
        validators=[RegexValidator(
            regex="^(\+\d{1,3})?,?\s?\d{8,13}",
            message='Veuillez entrer un numéro de téléphone valide au format +999999999999.',
        )],
    )

    subject = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Sujet de votre message'}),
        validators=[RegexValidator(
            regex="^[a-zA-Z ]*$",
            message='Veuillez entrer un sujet valide! Pas de chiffres ni caractères speciaux.',
        )],
    )

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'autofocus': True,
                'class': 'form-control',
                'placeholder': 'Votre nom complet'}
        )
    )
