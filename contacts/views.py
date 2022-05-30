from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.models import MyUser
from .models import Contact
from django.core.mail import send_mail


def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        region = request.POST['region']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        price = request.POST['price']
        price_new = request.POST['price_new']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'Ви вже відправляли запит на це авто раніше, очікуйте на відповідь!')
                return redirect('/cars/' + car_id)

        contact = Contact(car_id=car_id,
                          car_title=car_title,
                          user_id=user_id,
                          first_name=first_name,
                          last_name=last_name,
                          customer_need=customer_need,
                          city=city,
                          region=region,
                          email=email,
                          phone=phone,
                          message=message,
                          price=price,
                          price_new=price_new,
                          )

        """
        admin_info = MyUser.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
            'Запит на авто',
            'Ви маєте новий запит на авто' + car_title + 'Перевірте адмін панель',
            'sanyavenger100@gmail.com',
            [admin_email],
            fail_silently=False,
        )
        """

        contact.save()
        messages.success(request, 'Ваш запит надіслано!')
        return redirect('/cars/' + car_id)
