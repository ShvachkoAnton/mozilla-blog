from django import forms
from app.models import Profile
from django.contrib.auth.forms import UserCreationForm
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
class UserRegistrationForm(UserCreationForm):
    username=forms.CharField(label="Имя")
    password1=forms.CharField(label="Введите пароль",widget=forms.PasswordInput)
    password2=forms.CharField(label="Повторите пароль",widget=forms.PasswordInput)