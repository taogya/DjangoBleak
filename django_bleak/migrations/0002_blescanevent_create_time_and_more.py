# Generated by Django 4.2.2 on 2023-06-22 07:24

from django.db import migrations, models
import django_bleak.models.scanner


class Migration(migrations.Migration):

    dependencies = [
        ('django_bleak', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blescanevent',
            name='create_time',
            field=models.FloatField(blank=True, default=None, help_text='null means no process exists.', null=True, verbose_name='create time'),
        ),
        migrations.AlterField(
            model_name='blescanfilter',
            name='manufacturer_data',
            field=django_bleak.models.scanner.RegexField(blank=True, default=None, help_text='^626C65(34|35)2E30$', max_length=1024, null=True, verbose_name='regex of manufacturer_data'),
        ),
        migrations.AlterField(
            model_name='blescanfilter',
            name='service_data',
            field=django_bleak.models.scanner.RegexField(blank=True, default=None, help_text='^626C65(34|35)2E30$', max_length=1024, null=True, verbose_name='regex of service_data'),
        ),
    ]
