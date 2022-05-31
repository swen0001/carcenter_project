from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import MyUser
from .models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.core.paginator import Paginator


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    paginator = Paginator(all_cars, 3)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    brand_search = Car.objects.values_list('brand', flat=True).distinct()
    region_search = Car.objects.values_list('region', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': paged_cars,
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



def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        email_subject = 'У Вас нове повідомлення' + subject
        message_body = "Ім'я: " + name + ', Email: ' + email + ', Телефон: ' + phone + ', Повідомлення: ' + message

        admin_info = MyUser.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
                email_subject,
                message_body,
                'sanyavenger23@gmail.com',
                [admin_email],
                fail_silently=False,

            )
        messages.success(request, "Дякую за повідомлення, ми з Вами зв`яжимось")
        return redirect('contacts')
    return render(request, 'home/contacts.html')

