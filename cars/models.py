from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


class Car(models.Model):

    region_choice = (
        ('AK', 'Кримcька'),
        ('AA', 'Київська'),
        ('AB', 'Вінницька'),
        ('AC', 'Волинська'),
        ('AE', 'Дніпропетровька'),
        ('AH', 'Донецька'),
        ('AM', 'Житомирська'),
        ('AO', 'Закарпатська'),
        ('AP', 'Запорізьська'),
        ('AT', 'Івано-Франківська'),
        ('AX', 'Харківська'),
        ('BA', 'Кіровоградська'),
        ('BB', 'Луганська'),
        ('BC', 'Львівська'),
        ('BE', 'Миколаївська'),
        ('BH', 'Одеська'),
        ('BI', 'Полтавська'),
        ('BK', 'Рівненська'),
        ('BM', 'Сумська'),
        ('BO', 'Тернопільська'),
        ('BT', 'Херсонська'),
        ('BX', 'Хмельницька'),
        ('CA', 'Черкаська'),
        ('CB', 'Чернівецька'),
        ('CE', 'Чернігівська'),
    )

    year_choice = []
    for r in range(1995, (datetime.now().year + 1)):
        year_choice.append((r, r))

    features_choices = (
        ('Cruise Control', 'Круїз-контроль'),
        ('Audio Interface', 'Аудіоінтерфейс'),
        ('Airbags', 'Подушки безпеки'),
        ('Air Conditioning', 'Кондиціонер'),
        ('Seat Heating', 'Обігрів сидінь'),
        ('Alarm System', 'Сигналізація'),
        ('ParkAssist', 'Парктронік'),
        ('Power Steering', 'Гідропідсилювач керма'),
        ('Reversing Camera', 'Камера заднього виду'),
        ('Auto Start/Stop', 'Система Старт/Стоп'),
        ('Rain sensor', 'Сенсор дощу'),
        ('Bluetooth Handset', 'Bluetooth'),
    )

    body_style_choices = (
        ('1', 'Хетчбек'),
        ('2', 'Седан'),
        ('3', 'Позашляховик'),
        ('4', 'Універсал'),
        ('5', 'Купе'),
        ('6', 'Кабріолет'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    fuel_type_choices = (
        ('1', 'Дизель'),
        ('2', 'Бензин'),
        ('3', 'Бензин/Газ'),
        ('4', 'Газ'),
        ('5', 'Електро')
    )

    transmission_choices = (
        ('Mechanics', 'Механіка'),
        ('Automatic', 'Автоматична')
    )

    car_title = models.CharField(max_length=250)
    region = models.CharField(choices=region_choice, max_length=100)
    city = models.CharField(max_length=150, blank=True)
    color = models.CharField(max_length=150, blank=True)
    model = models.CharField(max_length=150, blank=True)
    year = models.IntegerField(('year'), choices=year_choice)
    price = models.IntegerField()
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