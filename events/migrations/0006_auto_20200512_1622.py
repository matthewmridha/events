# Generated by Django 3.0.5 on 2020-05-12 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200428_1442'),
        ('events', '0005_event_sport'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='Events',
        ),
    ]
