# Generated by Django 4.0.4 on 2022-05-29 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_team_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(upload_to='teams/%Y/%m/%d/'),
        ),
    ]