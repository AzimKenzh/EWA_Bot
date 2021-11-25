from django.db import models


class Ebay(models.Model):
    title = models.CharField(max_length=800, verbose_name='Название', blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Walmart(models.Model):
    title = models.CharField(max_length=800, verbose_name='Название', blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Amazon(models.Model):
    title = models.CharField(max_length=800, verbose_name='Название', blank=True, null=True)
    url = models.URLField(max_length=900, blank=True, null=True)

    def __str__(self):
        return self.title
