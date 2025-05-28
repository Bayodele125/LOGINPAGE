from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate



# Create your views here.

def register_view(request):
    error_message = None
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            error_message = "Passwords do not match."
        elif not email or not password1:
            error_message = "Email and password are required."
        else:
            from core.models import User
            try:
                user = User.objects.create_user(email=email, password=password1, first_name=first_name, last_name=last_name)
                login(request, user)
                return redirect('home')
            except Exception as e:
                error_message = str(e)

    return render(request, 'core/register.html', {'error_message': error_message})

def login_view(request):
    error_message = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            allowed_url = 'https://sites.google.com/view/visual-data/home'
            return redirect(allowed_url)
        else:
            error_message = 'Invalid email or password'
    return render(request, 'core/login.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    return render(request, 'core/home.html')
