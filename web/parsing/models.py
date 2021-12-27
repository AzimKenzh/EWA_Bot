from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
import firebase_admin
from firebase_admin import credentials, firestore


certificate_location = './firebase/ewa-bot-d54ca-firebase-adminsdk-zj7gl-5ce88f753c.json'
cred = credentials.Certificate(certificate_location)
firebase_admin.initialize_app(cred)
DB = firestore.client()
FIREBASE_COLLECTION = DB.collection('items')


class ImportExcels(models.Model):
    STATUS = [
        ('1', 'imported'),
        ('2', 'parsing'),
        ('3', 'parsed'),
    ]
    title = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=5000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=25, choices=STATUS, default=STATUS[0][0])
    # company = models.CharField(max_length=200, blank=True, null=True, verbose_name='Название компании')
    # item_title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Название продукта')
    # unique_value = models.CharField(max_length=200, blank=True, null=True)
    # volume = models.CharField(max_length=200, blank=True, null=True, verbose_name='Объем')
    annotations = models.JSONField(blank=True, null=True)



@receiver(post_save, sender=ImportExcels)
def synchronise_firestore(sender, instance, **kwargs):
    document = FIREBASE_COLLECTION.document(str(instance.id))
    document.set({'status': instance.get_status_display(), 'title': instance.title, 'url': instance.url,
                  'created_at': instance.created_at, 'updated_at': instance.updated_at})


@receiver(pre_delete, sender=ImportExcels)
def synchronise_firestore_delete(sender, instance, using, **kwargs):
    document = FIREBASE_COLLECTION.document(str(instance.id))
    document.delete()


class Ebay(models.Model):
    product_title = models.ForeignKey(ImportExcels, on_delete=models.CASCADE, related_name='ebays', null=True)
    title = models.TextField(verbose_name='Название', blank=True, null=True)
    url = models.URLField(max_length=5000, blank=True, null=True)
    star = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    percent = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or ''

    class Meta:
        ordering = ('-quantity',)


class Amazon(models.Model):
    product_title = models.ForeignKey(ImportExcels, on_delete=models.CASCADE, related_name='amazons', null=True)
    title = models.TextField(verbose_name='Название', blank=True, null=True)
    url = models.URLField(max_length=5000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
