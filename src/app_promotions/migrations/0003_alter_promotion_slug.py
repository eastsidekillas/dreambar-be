# Generated by Django 5.1.6 on 2025-02-06 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_promotions', '0002_promotion_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='Слаг'),
        ),
    ]
