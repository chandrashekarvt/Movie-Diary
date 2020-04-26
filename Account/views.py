from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from Movies.views import showMovies


def index(request):
    return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        if 'Register' in request.POST:
            return render(request, 'register.html')
        elif 'Login' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect(showMovies)
            else:
                return render(request, 'login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'register.html', {'error': 'User already exists.'})
            except User.DoesNotExist:
                username = request.POST['username']
                password = request.POST['password2']
                user = User.objects.create_user(username=username, password=password)
                return redirect(index)
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/accounts/logout/')
