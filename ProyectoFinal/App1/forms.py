from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from App1.models import Avatar

class UserForm(forms.Form):

    name = forms.CharField(max_length=30)
    city = forms.CharField(max_length=30)
    age = forms.IntegerField()
    email = forms.EmailField()

class GamesForm(forms.Form):

    name = forms.CharField(max_length=30)
    developer = forms.CharField(max_length=30)
    popularity = forms.IntegerField()
    type = forms.CharField()

class CreatorsForm(forms.Form):

    username = forms.CharField(max_length=30)
    platforms = forms.CharField(max_length=30)
    subscriptions = forms.IntegerField()

class RegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']  

   