# Generated by Django 3.2.6 on 2022-01-24 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0031_amazon_similarity'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmazonAll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True, verbose_name='Название')),
                ('url', models.URLField(blank=True, max_length=5000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('similarity', models.IntegerField(blank=True, null=True, verbose_name='Сходство')),
                ('product_title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='amazons_all', to='parsing.importexcels')),
            ],
        ),
    ]
