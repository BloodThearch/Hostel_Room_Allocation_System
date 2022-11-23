from django.forms import ModelForm
from django import forms
from db.models import *
from django.contrib.admin.widgets import AdminDateWidget

class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = "__all__"
        widgets = {
            "startDate":forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
            "endDate":forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
            "minCGPA":forms.NumberInput(attrs={'type':'number', 'class':'form-control'}),
            "maxCGPA":forms.NumberInput(attrs={'type':'number', 'class':'form-control'}),
            "baseRate":forms.NumberInput(attrs={'type':'number', 'class':'form-control'}),
            "costWithAC":forms.NumberInput(attrs={'type':'number', 'class':'form-control'})
        }

class StudentRegistrationForm(ModelForm):
    class Meta:
        model = StudentAccount
        fields = "__all__"
        widgets = {
            "firstName":forms.TextInput(attrs={'type':'text','class':'form-control'}),
            "lastName":forms.TextInput(attrs={'type':'text','class':'form-control'}),
            "email":forms.TextInput(attrs={'type':'email','class':'form-control'}),
            "passwd":forms.TextInput(attrs={'type':'password','class':'form-control'}),
            "personalContactNo":forms.NumberInput(attrs={'type':'number','class':'form-control'}),
            "gender":forms.Select(attrs={'class':'form-control'}, choices=(('M', 'Male'),('F', 'Female'))),
            # Student related fields below
            "rollno":forms.NumberInput(attrs={'type':'number','class':'form-control'}),
            "branch":forms.Select(attrs={'class':'form-control'}, choices=(('BE', 'BE'),('BTECH', 'BTECH'))),
            "parentContactNo":forms.NumberInput(attrs={'type':'number','class':'form-control'}),
            "CGPA":forms.NumberInput(attrs={'type':'number','class':'form-control'}),
        }

class StaffRegistrationForm(ModelForm):
    class Meta:
        model = StaffAccount
        fields = "__all__"
        widgets = {
            "firstName":forms.TextInput(attrs={'type':'text','class':'form-control'}),
            "lastName":forms.TextInput(attrs={'type':'text','class':'form-control'}),
            "email":forms.TextInput(attrs={'type':'email','class':'form-control'}),
            "passwd":forms.TextInput(attrs={'type':'password','class':'form-control'}),
            "personalContactNo":forms.NumberInput(attrs={'type':'number','class':'form-control'}),
            "gender":forms.Select(attrs={'class':'form-control'}, choices=(('M', 'Male'),('F', 'Female'))),
            # Staff related fields below
            "staffID":forms.NumberInput(attrs={'type':'number','class':'form-control'}),
        }