from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


class Car(models.Model):

    region_choice = (
        ('Кримcька', 'Кримcька'),
        ('Київська', 'Київська'),
        ('Вінницька', 'Вінницька'),
        ('Волинська', 'Волинська'),
        ('Дніпропетровька', 'Дніпропетровька'),
        ('Донецька', 'Донецька'),
        ('Житомирська', 'Житомирська'),
        ('Закарпатська', 'Закарпатська'),
        ('Запорізьська', 'Запорізьська'),
        ('Івано-Франківська', 'Івано-Франківська'),
        ('Харківська', 'Харківська'),
        ('Кіровоградська', 'Кіровоградська'),
        ('Луганська', 'Луганська'),
        ('Львівська', 'Львівська'),
        ('Миколаївська', 'Миколаївська'),
        ('Одеська', 'Одеська'),
        ('Полтавська', 'Полтавська'),
        ('Рівненська', 'Рівненська'),
        ('Сумська', 'Сумська'),
        ('Тернопільська', 'Тернопільська'),
        ('Херсонська', 'Херсонська'),
        ('Хмельницька', 'Хмельницька'),
        ('Черкаська', 'Черкаська'),
        ('Чернівецька', 'Чернівецька'),
        ('Чернігівська', 'Чернігівська'),
    )

    year_choice = []
    for r in range(1995, (datetime.now().year + 1)):
        year_choice.append((r, r))

    features_choices = (
        ('Круїз-контроль', 'Круїз-контроль'),
        ('Аудіоінтерфейс', 'Аудіоінтерфейс'),
        ('Подушки безпеки', 'Подушки безпеки'),
        ('Кондиціонер', 'Кондиціонер'),
        ('Обігрів сидінь', 'Обігрів сидінь'),
        ('Сигналізація', 'Сигналізація'),
        ('Парктронік', 'Парктронік'),
        ('Гідропідсилювач керма', 'Гідропідсилювач керма'),
        ('Камера заднього виду', 'Камера заднього виду'),
        ('Система Старт/Стоп', 'Система Старт/Стоп'),
        ('Сенсор дощ', 'Сенсор дощу'),
        ('Bluetooth', 'Bluetooth'),
    )

    body_style_choices = (
        ('Хетчбек', 'Хетчбек'),
        ('Седан', 'Седан'),
        ('Позашляховик', 'Позашляховик'),
        ('Універсал', 'Універсал'),
        ('Купе', 'Купе'),
        ('Кабріолет', 'Кабріолет'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    fuel_type_choices = (
        ('Дизель', 'Дизель'),
        ('Бензин', 'Бензин'),
        ('Бензин/Газ', 'Бензин/Газ'),
        ('Газ', 'Газ'),
        ('Електро', 'Електро')
    )

    transmission_choices = (
        ('Механіка', 'Механіка'),
        ('Автомат', 'Автомат')
    )

    car_title = models.CharField(max_length=250)
    region = models.CharField(choices=region_choice, max_length=100)
    city = models.CharField(max_length=150, blank=True)
    color = models.CharField(max_length=150, blank=True)
    model = models.CharField(max_length=150, blank=True)
    year = models.IntegerField(('year'), choices=year_choice)
    price = models.IntegerField()
    price_new = models.IntegerField(blank=True, default=0)
    description = RichTextField(blank=True)
    features = MultiSelectField(choices=features_choices, blank=True)
    body_style = models.CharField(choices=body_style_choices, max_length=150, blank=True)
    engine = models.CharField(max_length=150, blank=True)
    transmission = models.CharField(choices=transmission_choices, max_length=150, blank=True)
    kilometers = models.IntegerField(blank=True)
    doors = models.CharField(choices=door_choices, max_length=10, blank=True)
    passengers = models.IntegerField(blank=True)
    vin_code = models.CharField(max_length=150, blank=True)
    fuel_type = models.CharField(choices=fuel_type_choices, max_length=150, blank=True)
    phone_owners = models.CharField(max_length=150)
    is_featured = models.BooleanField()
    created_date = models.DateTimeField(default=datetime.now)
    car_photo_1 = models.ImageField(upload_to='photo/%Y/%m/%d/')
    car_photo_2 = models.ImageField(upload_to='photo/%Y/%m/%d/')
    car_photo_3 = models.ImageField(upload_to='photo/%Y/%m/%d/')
    car_photo_4 = models.ImageField(upload_to='photo/%Y/%m/%d/')
    car_photo_5 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    car_photo_6 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    car_photo_7 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    car_photo_8 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    car_photo_9 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    car_photo_10 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)


    def __str__(self):
        return self.car_title