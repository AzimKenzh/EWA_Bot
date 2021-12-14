from django.db import models


class ImportExcels(models.Model):
    STATUS = [
        ('1', 'imported'),
        ('2', 'edited'),
        ('3', 'parsing'),
        ('4', 'parsed'),
    ]
    title = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=5000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, choices=STATUS, default=STATUS[0][0])
    active = models.BooleanField(default=True)


class Ebay(models.Model):
    product_title = models.ForeignKey(ImportExcels, on_delete=models.SET_NULL, related_name='ebays', null=True)
    title = models.TextField(verbose_name='Название', blank=True, null=True)
    url = models.URLField(max_length=5000, blank=True, null=True)
    star = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    percent = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or ''

    class Meta:
        ordering = ('-quantity',)


class Amazon(models.Model):
    product_title = models.ForeignKey(ImportExcels, on_delete=models.SET_NULL, related_name='amazons', null=True)
    title = models.TextField(verbose_name='Название', blank=True, null=True)
    url = models.URLField(max_length=5000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

