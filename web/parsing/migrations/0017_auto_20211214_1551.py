# Generated by Django 3.2.6 on 2021-12-14 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0016_auto_20211213_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebay',
            name='percent',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ebay',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ebay',
            name='star',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]