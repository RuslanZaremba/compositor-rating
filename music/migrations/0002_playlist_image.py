# Generated by Django 3.0.8 on 2020-07-29 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='image',
            field=models.ImageField(default=0, upload_to='', verbose_name='картинка'),
            preserve_default=False,
        ),
    ]
