# Generated by Django 3.0.5 on 2020-04-21 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200421_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sport',
            field=models.ManyToManyField(help_text='Select all that apply', to='users.Sport'),
        ),
    ]
