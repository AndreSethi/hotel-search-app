# Generated by Django 4.0.5 on 2022-06-18 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amenities',
            options={'verbose_name_plural': 'Amenities'},
        ),
        migrations.AlterModelOptions(
            name='hotels',
            options={'verbose_name_plural': 'Hotels'},
        ),
    ]
