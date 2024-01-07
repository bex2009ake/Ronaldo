from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *



class AuthorForm(UserCreationForm):
    class Meta:
        model = Author
        fields = ['username','img','date','addres','zip_code','desc','email','phone','password1','password2']

        widgets = {
            'username': forms.TextInput(attrs={'id':'username','name':'username','class':'username'}),
            'date': forms.DateTimeInput(attrs={'id':'date','name':'date','class':'date'}),
            'addres': forms.TextInput(attrs={'id':'address','name':'address','class':'address'}),
            'zip_code': forms.NumberInput(attrs={'id':'zip_code','name':'zip_code','class':'zip_code'}),
            'phone': forms.TextInput(attrs={'id':'phone','name':'phone','class':'phone'}),
            'desc': forms.Textarea(attrs={'id':'desc','name':'desc','class':'desc'}),
            'img': forms.FileInput(attrs={'id':'img','name':'img','class':'img'}),
            'password1': forms.TextInput(attrs={'id':'password1','name':'password1','class':'password1'}),
            'password2': forms.TextInput(attrs={'id':'password2','name':'password2','class':'password2'}),
        }


class AuthorLoginForm(AuthenticationForm):
    class Meta:
        model = Author
        fields = ['username','password']

        widgets = {
            'username': forms.TextInput(attrs={'id':'username','name':'username','class':'username'}),
            'password': forms.TextInput(attrs={'id':'password','name':'password','class':'password'}),
        }


class WorkForm(forms.ModelForm):
    class Meta:
        model = Works
        fields = ['name','img']


        widgets = {
            'name': forms.TextInput(attrs={'id':'name','name':'name','class':'name'}),
            'img': forms.FileInput(attrs={'id':'img','name':'img','class':'img'}),
        }


class EducatekForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['title','desc','from_date','to_date']


        widgets = {
            'title': forms.TextInput(attrs={'id':'title','name':'title','class':'title','placeholder':'Title'}),
            'desc': forms.Textarea(attrs={'id':'desc','name':'desc','class':'desc','placeholder':'Description'}),
            'from_date': forms.TextInput(attrs={'id':'date_from','name':'date_from','class':'date_from','placeholder':'From'}),
            'to_date': forms.TextInput(attrs={'id':'date_to','name':'date_to','class':'date_to','placeholder':'To'}),
        }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title','desc','from_date','to_date']


        widgets = {
            'title': forms.TextInput(attrs={'id':'title','name':'title','class':'title','placeholder':'Title'}),
            'desc': forms.Textarea(attrs={'id':'desc','name':'desc','class':'desc','placeholder':'Description'}),
            'from_date': forms.TextInput(attrs={'id':'date_from','name':'date_from','class':'date_from','placeholder':'From'}),
            'to_date': forms.TextInput(attrs={'id':'date_to','name':'date_to','class':'date_to','placeholder':'To'}),
        }


class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ['title','desc','from_date','to_date']


        widgets = {
            'title': forms.TextInput(attrs={'id':'title','name':'title','class':'title','placeholder':'Title'}),
            'desc': forms.Textarea(attrs={'id':'desc','name':'desc','class':'desc','placeholder':'Description'}),
            'from_date': forms.TextInput(attrs={'id':'date_from','name':'date_from','class':'date_from','placeholder':'From'}),
            'to_date': forms.TextInput(attrs={'id':'date_to','name':'date_to','class':'date_to','placeholder':'To'}),
        }
