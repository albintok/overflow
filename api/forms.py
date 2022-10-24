from pyexpat import model
from django import forms
from api.models import MyUser
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model=MyUser
        fields=["first_name","last_name","username","email","pro_pic","phone","password1","password2"]
        


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))