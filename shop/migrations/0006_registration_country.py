# Generated by Django 5.0.6 on 2024-11-29 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='Country',
            field=models.CharField(default='', max_length=500),
        ),
    ]
