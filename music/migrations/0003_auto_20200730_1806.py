# Generated by Django 3.0.8 on 2020-07-30 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_playlist_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='count_tracks',
            field=models.PositiveIntegerField(default=0, verbose_name='Колличество композиций'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='playlist',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='картинка'),
        ),
    ]
