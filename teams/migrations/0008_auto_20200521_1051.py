# Generated by Django 3.0.5 on 2020-05-21 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_auto_20200521_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]