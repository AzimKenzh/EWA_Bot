from django.db import models


class Ebay(models.Model):
    title = models.CharField(max_length=800, verbose_name='Название', blank=True, null=True)
    # condition = models.CharField(max_length=500, verbose_name='Состояние товара', blank=True, null=True)
    # quantity = models.IntegerField(verbose_name='Количество', blank=True, null=True)
    # star = models.IntegerField(verbose_name='Звездочки', blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title