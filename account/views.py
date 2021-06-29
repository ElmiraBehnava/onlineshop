from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
# Create the user profile
from .models import Profile

from cart.cart import Cart


#message for updatin 
from django.contrib import messages







def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            a = form.save()
            # Create the user profile
            
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            
            Profile.objects.create(user=a)
            login(request, user)

            return redirect('/details/home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
    


@login_required
def dashboard(request):
    cart= Cart(request)
    return render(request,'registration/dashboard.html',{'section': 'dashboard', 'cart': cart})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm( instance=request.user.profile, data=request.POST, files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'تغییرات پروفایل شما با موفقیت انجام شد.')
        
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'registration/edit.html', {'user_form': user_form, 'profile_form': profile_form})


