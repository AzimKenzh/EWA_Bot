# Generated by Django 3.2.6 on 2021-12-13 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0014_alter_importexcels_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importexcels',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]