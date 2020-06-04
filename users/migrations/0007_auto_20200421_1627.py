# Generated by Django 3.0.5 on 2020-04-21 10:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200421_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default='dhaka', max_length=164),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.CharField(default='Bangladesh', max_length=164),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number must be valid', regex='^\\+?88?\\d{9,15}$')]),
        ),
    ]