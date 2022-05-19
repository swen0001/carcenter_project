from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def cars(request):
    return render(request, 'home/about.html')


def contacts(request):
    return render(request, 'home/contacts.html')


def news(request):
    return render(request, 'home/news.html')
