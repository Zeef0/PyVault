from .models import Vault, Info
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class VaultForm(forms.ModelForm):
    class Meta:
        model = Info
        fields =  ["account", "username", "email", "password"]

        widgets = {
            "password": forms.PasswordInput()
        }