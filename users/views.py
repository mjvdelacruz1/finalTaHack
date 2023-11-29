from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm

from django.contrib import messages

def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('paths:landing')    
        else:
            messages.info(request, 'Username OR Password is incorrect.')
            
    context = {}
    return render(request, 'users/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('users:loginView')


def signup(request):
    form = CreateUserForm()
    
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Succesfully created an account for ' +user)
            
            return redirect('users:loginView')
            
    context = {'form': form}
    
    return render (request,'users/signup.html', context)