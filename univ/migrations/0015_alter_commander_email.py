# Generated by Django 5.0.1 on 2024-10-06 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univ', '0014_alter_commander_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commander',
            name='email',
            field=models.EmailField(default='bienvenu@gmail.com', max_length=254),
        ),
    ]
