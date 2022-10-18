from django import forms
from django.contrib.auth.models import User

from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'fullName',
            'adress',
            'zip_code',
            'city',
            'email',
            'phone',
            'date',
            'hour',
            'message',
            'user',
        ]
