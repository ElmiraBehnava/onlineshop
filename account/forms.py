from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from .models import Profile
#creating userprofile
from django.forms import ModelForm



# class UserEditForm(AuthenticationForm):
#     username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'نام کاربری'}))
#     email = forms.EmailField(label="",widget=forms.TextInput(attrs={'placeholder':'ایمیل را وارد کنید... '}))

class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'نام'}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'نام خانوادگی'}))
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'placeholder':'ایمیل را وارد کنید... '}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')



sex_choice = [('F', 'خانم'), ('M', 'آقا'),]
class ProfileEditForm(forms.ModelForm):
    sex = forms.ChoiceField(label=False, widget=forms.RadioSelect, choices=sex_choice)
    
    date_of_birth = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'نام خانوادگی'}))
    class Meta:
        model = Profile
        fields = ('sex','date_of_birth')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'نام کاربری'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور'}))
    


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'نام کاربری'}))
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'placeholder':'ایمیل را وارد کنید... '}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'تکرار رمز عبور '}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class AccountChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور قدیمی'}))
    new_password1 = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور جدید'}))
    new_password2 = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder':' تکرار رمز عبور جدید'}))
    
    







    