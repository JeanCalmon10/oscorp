from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm

from .models import Product


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(help_text='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(help_text='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(help_text='', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image_url']