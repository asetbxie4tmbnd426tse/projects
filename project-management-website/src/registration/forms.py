from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
