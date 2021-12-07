from typing import Text
from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import fields
from django.forms import ModelForm, widgets
from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import *
from django.db.models.deletion import PROTECT
from home.models import *


class RegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={ 'style': 'height: 50px;','class': 'form-control'}),
        label='Username', max_length=15)
    email= forms.EmailField(widget=forms.EmailInput(attrs={'style': 'height: 50px;','class': 'form-control'}),label='Email')
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'style':'height: 50px;','class': 'form-control'}))
    password2=forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'style':'height: 50px;','class': 'form-control'}))

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1= self.cleaned_data['password1']
            password2= self.cleaned_data['password2']
            if password1==password2 and password1:
                return password2
        raise forms.ValidationError("Invalid password")
    
    def clean_username(self):
        username= self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Username contains special characters")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Username already exists")

    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email= self.cleaned_data['email'], password=self.cleaned_data['password1'])
######################################################

class createProjectForm(forms.ModelForm):
    class Meta: 
        model= Project
        fields=('name_project','decription','group','deadline')
        
        widgets={
            'name_project':forms.TextInput(attrs={'class': 'form-control' }),
            'decription': forms.TextInput(attrs={ 'class': 'form-control'}),
            # 'group': forms.TextInput(attrs={ }),
            'deadline': forms.NumberInput(attrs={ 'type':'date','class': 'form-control'}),
        }
######################################################

class updateProjectForm(forms.ModelForm):
    class  Meta:
        model = Project
        fields=('name_project','decription','deadline','status')
        CHOICES=(
        ('1','Complete'),
        ('0','Incomplete ')
        )
        widgets={
            'name_project': forms.TextInput(attrs={ 'style': 'width: 70%;','class': 'form-control'}),
            'decription': forms.TextInput(attrs={ 'style': 'width: 70%;','class': 'form-control'}),
            'deadline': forms.NumberInput(attrs={ 'type':'date','style': 'width: 70%;','class': 'form-control'}),
            'status': forms.Select(attrs={ 'style': 'width: 70%;','class': 'form-control'},choices=CHOICES),
        }
######################################################

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model= User
        fields=['username']
        widgets={
            'username':forms.TextInput(attrs={ 'style': 'width: 70%;','class': 'form-control'}),
        }
######################################################

class editProfileForm(forms.ModelForm):
    
    class  Meta:
        model = Profile
        fields=('lastname','firstname','gender','birth','bio','avatar')
        CHOICES=(
        ('Female','Female'),
        ('Male','Male'),
        ('Other','Other')
    )
        widgets={
            'lastname': forms.TextInput(attrs={ 'style': 'width: 70%;','class': 'form-control'}),
            'firstname': forms.TextInput(attrs={ 'style': 'width: 70%;','class': 'form-control'}),
            'birth': forms.NumberInput(attrs={ 'type':'date','style': 'width: 70%;','class': 'form-control'}),
            'gender': forms.Select(attrs={ 'style': 'width: 70%;','class': 'form-control'},choices=CHOICES),
            'bio': forms.TextInput(attrs={ 'style': 'width: 70%;','class': 'form-control'}),
            'avatar':forms.FileInput(attrs={'class': 'form-control-file'}),
        }
######################################################

class createTaskForm(forms.ModelForm):
    class Meta:
        model= Task
        fields=('project','task','decription','deadline')
        read_only_fields=('project')
        widgets={
            'project':forms.TextInput(attrs={ 'class': 'form-control','id':'disabledTextInput'}),
            'task': forms.TextInput(attrs={ 'class': 'form-control'}),
            'decription': forms.TextInput(attrs={ 'class': 'form-control'}),
            'deadline': forms.NumberInput(attrs={ 'type':'date','class': 'form-control '}),
        }
######################################################
    
class updateTaskForm(forms.ModelForm):
    class  Meta:
        model = Task
        fields=('task','decription','deadline','status')
        
        CHOICES=(
        ('1','Complete'),
        ('0','Incomplete ')
        )
        widgets={
            'task': forms.TextInput(attrs={ 'class': 'form-control'}),
            'decription': forms.TextInput(attrs={ 'class': 'form-control'}),
            'deadline': forms.NumberInput(attrs={ 'type':'date','class': 'form-control'}),
            'status': forms.Select(attrs={ 'class': 'form-control'},choices=CHOICES),
        }
######################################################
