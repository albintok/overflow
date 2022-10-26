from pyexpat import model
from django import forms
from api.models import MyUser,Questions
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
        password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
        password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
        class  Meta:
           model=MyUser
           fields=["first_name","last_name","username","email","pro_pic","phone","password1","password2"]
           widgets={"first_name":forms.TextInput(attrs={"class":"form-control"}),
                   "last_name":forms.TextInput(attrs={"class":"form-control"}),
                    "username":forms.TextInput(attrs={"class":"form-control"}),
                    "email":forms.TextInput(attrs={"class":"form-control"}),
                    "pro_pic":forms.FileInput(attrs={"class":"form-control"}),
                    }
        


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class QuestinForm(forms.ModelForm):
    class Meta:
        model=Questions
        fields=["questin","image"]

        widgets={"questin":forms.Textarea(attrs={"class":"form-control","rows":3}),
                "image":forms.FileInput(attrs={"class":"form-select"}),
                }