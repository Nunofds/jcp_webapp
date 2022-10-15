from django import forms
from reservation.models import Reservation


class ReservationForm(forms.Form):

    class Meta:
        model: Reservation

    fullName = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'validate'}),
    )

    adress = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'validate'}),
    )

    zip_code = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'validate'}),
    )

    city = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'validate'}),
    )

    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'validate'}),
    )

    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'validate'}),
    )

    date = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'validate'}),
    )

    hour = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'validate'}),
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
