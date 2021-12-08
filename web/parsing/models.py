from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField


class Ebay(models.Model):
    title = models.CharField(max_length=800, verbose_name='Название', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or ''


class Amazon(models.Model):
    title = models.CharField(max_length=800, verbose_name='Название', blank=True, null=True)
    url = models.URLField(max_length=900, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Walmart(models.Model):
    title = models.CharField(max_length=800, verbose_name='Название', blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class ImportExcels(models.Model):
    title = ArrayField(models.CharField(max_length=400), blank=True, null=True)

#todo: export excel