from django.shortcuts import render
from .models import Team
from cars.models import Car


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')

    brand_search = Car.objects.values_list('brand', flat=True).distinct()
    region_search = Car.objects.values_list('region', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'brand_search': brand_search,
        'region_search': region_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
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
