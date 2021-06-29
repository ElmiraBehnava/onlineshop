from .models import Comment
from django import forms
from . import models




class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'*نام'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'*ایمیل'} ))
    body = forms.CharField(max_length=300,widget=forms.Textarea(attrs={'placeholder':'*نقد خود را ثبت کنید...'}))
    class Meta:
        model = models.Comment
        fields = ('name', 'email', 'body')


