from django.db import models


class Book(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    descriptions = models.TextField(verbose_name='Описание')
    
