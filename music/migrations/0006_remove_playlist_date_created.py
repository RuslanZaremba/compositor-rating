# Generated by Django 3.0.8 on 2020-07-30 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_playlist_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='date_created',
        ),
    ]
