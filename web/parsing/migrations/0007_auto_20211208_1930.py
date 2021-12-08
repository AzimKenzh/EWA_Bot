# Generated by Django 3.2.6 on 2021-12-08 13:30

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0006_importexcel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportExcels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=None)),
            ],
        ),
        migrations.DeleteModel(
            name='ImportExcel',
        ),
    ]
