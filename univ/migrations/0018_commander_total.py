# Generated by Django 5.0.1 on 2024-10-20 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univ', '0017_etudiant_prix'),
    ]

    operations = [
        migrations.AddField(
            model_name='commander',
            name='total',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]