# Generated by Django 5.0.1 on 2024-01-28 07:33

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univ', '0006_alter_etudiant_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='filiere',
            field=models.CharField(default='SRI', max_length=70),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='parcours',
            field=models.CharField(default='Math', max_length=70),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='tel',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+242064036047', max_length=128, null=True, region=None),
        ),
    ]