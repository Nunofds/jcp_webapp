from django import forms
from .models import Contact


class ContactForm(forms.Form):
    class Meta:
        model: Contact

    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Votre nom complet'})
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
