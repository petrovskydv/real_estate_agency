# Generated by Django 2.2.4 on 2021-04-04 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20210404_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
