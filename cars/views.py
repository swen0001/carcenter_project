from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger


def cars(request):

    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    brand_search = Car.objects.values_list('brand', flat=True).distinct()
    region_search = Car.objects.values_list('region', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'cars': paged_cars,
        'brand_search': brand_search,
        'region_search': region_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'cars/cars.html', data)


def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)

    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_detail.html', data)


def search(request):
    cars = Car.objects.order_by('-created_date')

    brand_search = Car.objects.values_list('brand', flat=True).distinct()
    region_search = Car.objects.values_list('region', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    fuel_type_search = Car.objects.values_list('fuel_type', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'brand' in request.GET:
        brand = request.GET['brand']
        if brand:
            cars = cars.filter(brand__iexact=brand)

    if 'region' in request.GET:
        region = request.GET['region']
        if region:
            cars = cars.filter(region__iexact=region)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'fuel_type' in request.GET:
        fuel_type = request.GET['fuel_type']
        if fuel_type:
            cars = cars.filter(fuel_type__iexact=fuel_type)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'cars': cars,
        'brand_search': brand_search,
        'region_search': region_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'fuel_type_search': fuel_type_search,
    }
    return render(request, 'cars/search.html', data)
