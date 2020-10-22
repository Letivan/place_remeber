from django.contrib.auth.models import User
from django.db import models
from geoposition.fields import GeopositionField


class Remember(models.Model):
    """The model for the storage of memories in the places you visit"""
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь', db_index=True)
    remember = models.TextField(verbose_name='Воспоминание')
    coordinate = GeopositionField(verbose_name='Координаты')

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'Воспоминание'
        verbose_name_plural = "Воспоминания"
        ordering = ('-date_create',)
