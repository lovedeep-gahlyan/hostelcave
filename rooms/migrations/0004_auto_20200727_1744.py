# Generated by Django 3.0.7 on 2020-07-27 12:14

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_auto_20200727_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='contact phone number', max_length=31),
        ),
    ]
