from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def login(request):
    return render(request, 'accounts/login.html ')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Нікнейм вже зайнято :(')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email вже зайнято :(')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname,
                                                    last_name=lastname,
                                                    username=username,
                                                    email=email,
                                                    password=password)
                    auth.login(request, user)
                    messages.success(request, 'Ваш аккаунт авторизовано :)')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request, 'Ви успішно зареєстровані')
                    return redirect('login')
        else:
            messages.error(request, 'Паролі не співпадають :(')
            return redirect('register')
    return render(request, 'accounts/register.html ')


def dashboard(request):
    return render(request, 'accounts/dashboard.html ')


def logout(request):
    return redirect('home')



