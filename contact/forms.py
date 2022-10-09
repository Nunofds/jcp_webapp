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
        validators=[RegexValidator(regex="^[a-zA-Z ]*$", message='Veuillez entrer un nom valide! Pas de chiffres ni caractères speciaux.')],
    )
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Votre email'}))
    phone = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Votre telephone'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Sujet de votre message'}))
    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Votre nom complet'})
    )
