# Generated by Django 5.0.1 on 2024-10-06 21:54

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('univ', '0013_alter_commander_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commander',
            name='tel',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+242064036047', max_length=128, region=None),
        ),
    ]