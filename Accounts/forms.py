from django import forms
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)


class StaffSignUp(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','first_name','last_name', 'email','password1','password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        r = User.objects.filter(username=username)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        id = User.objects.filter(email=email)
        if id.count():
            raise forms.ValidationError("Email address already exists.")
        return email

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control'})

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control','placeholder':'Password'
        }
    ))
