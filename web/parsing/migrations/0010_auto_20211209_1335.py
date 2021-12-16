# Generated by Django 3.2.6 on 2021-12-09 07:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0009_auto_20211209_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='importexcels',
            name='status',
            field=models.CharField(choices=[('imported', 'imported'), ('edited', 'edited'), ('parsing', 'parsing'), ('parsed', 'parsed')], default='imported', max_length=25),
        ),
        migrations.AddField(
            model_name='importexcels',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 9, 7, 35, 34, 391909, tzinfo=utc)),
            preserve_default=False,
        ),
    ]