# Generated by Django 3.2.6 on 2021-12-13 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0015_alter_importexcels_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazon',
            name='title',
            field=models.TextField(blank=True, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='ebay',
            name='title',
            field=models.TextField(blank=True, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='walmart',
            name='title',
            field=models.TextField(blank=True, null=True, verbose_name='Название'),
        ),
    ]
