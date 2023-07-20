# Generated by Django 4.2.2 on 2023-06-28 04:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_bleak', '0003_blescanevent_scan_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blescanfilter',
            name='company_code',
            field=models.IntegerField(blank=True, default=None, help_text='65535', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(65535)], verbose_name='company code'),
        ),
    ]