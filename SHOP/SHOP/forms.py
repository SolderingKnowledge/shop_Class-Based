from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()


class ContactForm(forms.Form):
    name    = forms.CharField()
    email   =forms.EmailField()
    content = forms.CharField()




class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)




class SignUpForm(forms.Form):
    username  = forms.CharField()
    email     = forms.CharField()
    password  = forms.CharField(widget=forms.PasswordInput)

