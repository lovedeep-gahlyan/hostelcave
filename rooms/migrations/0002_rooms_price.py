# Generated by Django 3.0.7 on 2020-07-26 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]