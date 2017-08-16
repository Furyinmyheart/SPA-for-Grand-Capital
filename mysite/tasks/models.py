from __future__ import unicode_literals

from django.db import models


class Task(models.Model):
    title = models.TextField(verbose_name='Задача', max_length=50)
    publication_date = models.DateField(verbose_name='Дата постановки', blank=True, null=True)
    author = models.TextField(verbose_name='Автор задачи', max_length=30, blank=True)

