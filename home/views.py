from django.shortcuts import render
from .models import Team


def home(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'home/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'home/about.html', data)


def cars(request):
    return render(request, 'home/about.html')


def contacts(request):
    return render(request, 'home/contacts.html')


def news(request):
    return render(request, 'home/news.html')
