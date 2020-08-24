from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class StudentForm(UserCreationForm):
    ID_No = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Student ID No'}),required=True, max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Firstname'}),required=True, max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lastname'}),required=True, max_length=50)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),required=True, max_length=50)
    department = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Class'}),required=True, max_length=50)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),required=True, max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),required=True, max_length=50)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Re-enter password'}),required=True, max_length=50)

    class Meta:
        model = User
        fields = ('ID_No','first_name','last_name','email','department','username','password1','password2')

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password != confirm_password:
            raise forms.ValidationError("Password Mismatch")
        return confirm_password

class TeacherForm(UserCreationForm):
    ID_No = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Teacher ID No'}),required=True, max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Firstname'}),required=True, max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lastname'}),required=True, max_length=50)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),required=True, max_length=50)
    department = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Department'}),required=True, max_length=50)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),required=True, max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),required=True, max_length=50)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Re-enter password'}),required=True, max_length=50)


    class Meta:
        model = User
        fields = ('ID_No','first_name','last_name','email','department','username','password1','password2')

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password != confirm_password:
            raise forms.ValidationError("Password Mismatch")
        return confirm_password


class UserLoginForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),required=True, max_length=50)
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),required=True, max_length=50)

class DocumentForm(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}), required=True, max_length=30)
    message = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Message'}), required=True, max_length=30)
    document = forms.FileField(label="")

    class Meta:
        model = Document
        fields = ('title', 'document', 'message')

class UserEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True, max_length=30)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True, max_length=30)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')