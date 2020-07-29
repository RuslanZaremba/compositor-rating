from django.db import models


class PlayList(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя пользователя')
    track_list = models.TextField(verbose_name='Список композиций', null=True)
    image = models.ImageField(verbose_name='картинка')