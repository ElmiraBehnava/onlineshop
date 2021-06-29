from django import forms
from .models import Order


CITY_CHOICES = [(1,'tehran'), (2, 'kashan')]


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField (label=False, max_length=50,  widget=forms.TextInput(attrs={'placeholder':'*نام'}))
    last_name = forms.CharField(label=False, max_length=50, widget=forms.TextInput(attrs={'placeholder':'* نام خانوادگی'}))
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder':'* آدرس ایمیل'}) , required=False)
    address = forms.CharField(label=False, max_length=300,widget=forms.TextInput(attrs={'placeholder':'آدرس خود را وارد کنید'}))
    postal_code = forms.IntegerField(label=False, widget=forms.TextInput(attrs={'placeholder':'کد پستی'}))
    city = forms.TypedChoiceField(label=False, choices=CITY_CHOICES, coerce = str)

    
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address','postal_code', 'city']
        