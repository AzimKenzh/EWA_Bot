# Generated by Django 3.2.6 on 2021-11-24 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0003_amazon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazon',
            name='url',
            field=models.URLField(blank=True, max_length=900, null=True),
        ),
    ]
