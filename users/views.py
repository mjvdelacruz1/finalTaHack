from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm

from django.contrib import messages

def loginPage(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password1')

        print("Email:", form)
        print("Password:", password)
        
        if form.is_valid():
            print("Password:", password)
            user = authenticate(request, username=email, password=password)
            print("Authenticated User:", user)  # Add this line to check the authenticated user
            if user is not None:
                print("done")
                login(request, user)
                return redirect('paths:landing.html')
    
    return render(request, 'users/login.html', {'form': form})

def signup(request):
    form = CustomUserCreationForm()
    
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Succesfully created an account for ' +user)
            
            return redirect('users:login')
            
    context = {'form': form}
    
    return render (request,'users/signup.html', context)