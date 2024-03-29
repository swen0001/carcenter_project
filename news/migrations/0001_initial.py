# Generated by Django 4.0.4 on 2022-05-30 12:12

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=250)),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('news_photo', models.ImageField(upload_to='news_auto/%Y/%m/%d/')),
            ],
        ),
    ]
