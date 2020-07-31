from django.db import models


class PlayList(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя пользователя')
    track_list = models.TextField(verbose_name='Список композиций', null=True)
    image = models.ImageField(verbose_name='картинка', null=True)
    count_tracks = models.PositiveIntegerField(verbose_name='Колличество композиций', default=0)
