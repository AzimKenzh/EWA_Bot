# Generated by Django 3.2.6 on 2022-01-26 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0032_amazonall'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proxies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proxy', models.CharField(max_length=100)),
            ],
        ),
    ]
