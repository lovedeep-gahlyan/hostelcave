# Generated by Django 3.0.7 on 2020-07-27 12:07

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_rooms_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='maplink',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rooms',
            name='phone',
            field=phone_field.models.PhoneField(default=1, max_length=31),
            preserve_default=False,
        ),
    ]
