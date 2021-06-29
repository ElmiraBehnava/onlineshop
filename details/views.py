from django.shortcuts import render
from shop.models import Category




def index(request):
    return render(request, "details/base.html",{})

def home(request):
        new_category = Category.objects.all()[:4]
        category_shortcut = Category.objects.all()[:10]
        num_category = Category.objects.all().count()
        return render(request, "details/home.html",{'new_category':new_category, 'category_shortcut':category_shortcut, 'num_category':num_category})

def about(request):
        return render(request, "details/about.html",{})

def contact(request):
        return render(request, "details/contact.html",{})

def fq(request):
        return render(request, "details/fq.html",{})

def privacy_policy(request):
        return render(request, "details/privacy_policy.html",{})