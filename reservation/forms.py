from django import forms
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
        ]
