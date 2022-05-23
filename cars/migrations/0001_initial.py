# Generated by Django 4.0.4 on 2022-05-21 11:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_title', models.CharField(blank=True, max_length=250)),
                ('region', models.CharField(blank=True, choices=[('AK', 'Кримcька'), ('AA', 'Київська'), ('AB', 'Вінницька'), ('AC', 'Волинська'), ('AE', 'Дніпропетровька'), ('AH', 'Донецька'), ('AM', 'Житомирська'), ('AO', 'Закарпатська'), ('AP', 'Запорізьська'), ('AT', 'Івано-Франківська'), ('AX', 'Харківська'), ('BA', 'Кіровоградська'), ('BB', 'Луганська'), ('BC', 'Львівська'), ('BE', 'Миколаївська'), ('BH', 'Одеська'), ('BI', 'Полтавська'), ('BK', 'Рівненська'), ('BM', 'Сумська'), ('BO', 'Тернопільська'), ('BT', 'Херсонська'), ('BX', 'Хмельницька'), ('CA', 'Черкаська'), ('CB', 'Чернівецька'), ('CE', 'Чернігівська')], max_length=100)),
                ('city', models.CharField(max_length=150)),
                ('color', models.CharField(max_length=150)),
                ('model', models.CharField(max_length=150)),
                ('year', models.IntegerField(blank=True, choices=[(1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], verbose_name='year')),
                ('price', models.IntegerField(blank=True)),
                ('description', models.TextField(max_length=500)),
                ('features', models.CharField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'), ('Bluetooth Handset', 'Bluetooth Handset')], max_length=100)),
                ('body_style', models.CharField(max_length=150)),
                ('engine', models.CharField(max_length=150)),
                ('transmission', models.CharField(max_length=150)),
                ('kilometers', models.IntegerField()),
                ('doors', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=150)),
                ('passengers', models.IntegerField(max_length=150)),
                ('vin_code', models.CharField(max_length=150)),
                ('fuel_type', models.CharField(max_length=150)),
                ('phone_owners', models.CharField(blank=True, max_length=150)),
                ('is_featured', models.BooleanField(max_length=150)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('car_photo_1', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/')),
                ('car_photo_2', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/')),
                ('car_photo_3', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/')),
                ('car_photo_4', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/')),
                ('car_photo_5', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('car_photo_6', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('car_photo_7', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('car_photo_8', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('car_photo_9', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('car_photo_10', models.ImageField(upload_to='photo/%Y/%m/%d/')),
            ],
        ),
    ]