# Generated by Django 3.0.5 on 2020-05-12 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_hostname_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.EventType'),
        ),
        migrations.AddField(
            model_name='event',
            name='host',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.HostName'),
        ),
    ]