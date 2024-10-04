from django import forms
from notes.models import Task
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):

    class Meta:

        model=Task

        # fields="__all__"

        # fields=["title","description",...]

        exclude=("created_date","status","updated_date")

        #styling django modelform
        widgets={

            "title":forms.TextInput(attrs={"class":"form-control"}),

            "description":forms.Textarea(attrs={"class":"form-control"}),

            "due_date":forms.DateInput(attrs={"class":"form-control","type":"date"}),  #cALENDER DISPLAY

            "category":forms.Select(attrs={"class":"form-control form-select"}),

            "user":forms.TextInput(attrs={"class":"form-control"})
        }



class RegistrationForm(forms.ModelForm):

    class Meta:

        model=User   

        fields=["username","email","password"]

        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.TextInput(attrs={"class":"form-control"})
            
        }

class SignInForm(forms.Form):

    username=forms.CharField()

    password=forms.CharField()