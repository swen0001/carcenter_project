# Generated by Django 4.0.4 on 2022-05-29 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_alter_contact_price_new'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='price_new',
            new_name='price_new1',
        ),
    ]
