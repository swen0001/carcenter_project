# Generated by Django 4.0.4 on 2022-05-29 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_alter_contact_price_new1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='price_new1',
            new_name='price_new',
        ),
    ]
