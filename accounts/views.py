from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import MyUser


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Ваш аккаунт авторизовано :)')
            return redirect('dashboard')
        else:
            messages.error(request, 'Логін або Пароль не вірний :(')
            return redirect('login')
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
            if MyUser.objects.filter(username=username).exists():
                messages.error(request, 'Нікнейм вже зайнято :(')
                return redirect('register')
            else:
                if MyUser.objects.filter(email=email).exists():
                    messages.error(request, 'Email вже зайнято :(')
                    return redirect('register')
                else:
                    user = MyUser.objects.create_user(first_name=firstname,
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
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Ви вийшли із свого аккаунта')
        return redirect('home')



