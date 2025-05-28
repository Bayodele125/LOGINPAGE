from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserCreationForm, UserLoginForm


# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    error_message = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid email or password'
    return render(request, 'core/login.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    return render(request, 'core/home.html')
