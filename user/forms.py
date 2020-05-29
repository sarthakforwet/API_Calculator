from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class FacultyResgistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password','email','first_name','last_name',]
    def __init__(self, *args, **kwargs):
        super(FacultyResgistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Faculty ID'})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}) 
        self.fields['password'].label = False
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'}) 
        self.fields['email'].label = False
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}) 
        self.fields['first_name'].label = False
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}) 
        self.fields['last_name'].label = False

class MyAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
    def __init__(self, *args, **kwargs):
        super(MyAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Faculty ID'})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}) 
        self.fields['password'].label = False