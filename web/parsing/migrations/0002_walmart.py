# Generated by Django 3.2.6 on 2021-11-20 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Walmart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=800, null=True, verbose_name='Название')),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
