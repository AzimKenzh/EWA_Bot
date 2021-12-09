from django.db import models


class ImportExcels(models.Model):
    STATUS = [
        ('imported', 'imported'),
        ('edited', 'edited'),
        ('parsing', 'parsing'),
        ('parsed', 'parsed'),
    ]
    title = models.CharField(max_length=400, blank=True, null=True)
    url = models.CharField(max_length=400, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, choices=STATUS, default=STATUS[0][0])
    active = models.BooleanField(default=True)


class Ebay(models.Model):
    product_title = models.ForeignKey(ImportExcels, on_delete=models.SET_NULL, related_name='ebays', null=True)
    title = models.CharField(max_length=800, verbose_name='Название', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or ''


class Amazon(models.Model):
    product_title = models.ForeignKey(ImportExcels, on_delete=models.SET_NULL, related_name='amazons', null=True)
    title = models.CharField(max_length=800, verbose_name='Название', blank=True, null=True)
    url = models.URLField(max_length=900, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Walmart(models.Model):
    product_title = models.ForeignKey(ImportExcels, on_delete=models.SET_NULL, related_name='walmarts', null=True)
    title = models.CharField(max_length=800, verbose_name='Название', blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
