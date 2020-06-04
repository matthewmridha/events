# Generated by Django 3.0.5 on 2020-05-19 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0012_auto_20200428_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=164)),
                ('logo', models.FileField(blank=True, upload_to='media/team_logos')),
                ('description', models.TextField(blank=True)),
                ('captain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_captain', to='users.UserProfile')),
                ('members', models.ManyToManyField(blank=True, related_name='team_member', to='users.UserProfile')),
            ],
        ),
    ]