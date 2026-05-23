from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm

def auth_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'login':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = User.objects.filter(email=email).first()
                
                if user:
                    user = authenticate(request, username=user.username, password=password)
                    if user:
                        login(request, user)
                        return redirect('home')
                
                form.add_error(None, 'Invalid email or password')
            return render(request, 'main/auth.html', {'login_form': form, 'active': 'login'})
        
        elif action == 'register':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')
            return render(request, 'main/auth.html', {'register_form': form, 'active': 'register'})
    
    login_form = LoginForm()
    register_form = RegisterForm()
    return render(request, 'main/auth.html', {'login_form': login_form, 'register_form': register_form})

def logout_view(request):
    logout(request)
    return redirect('auth')

def home(request):
    return render(request, 'main/home.html')

def animals(request):
    return render(request, 'main/animals.html')

def about(request):
    return render(request, 'main/about.html')