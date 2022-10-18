from django.contrib.auth import get_user_model
from django import forms


class UserUpdateProfile(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'email']

