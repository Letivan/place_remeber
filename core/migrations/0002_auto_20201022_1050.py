# Generated by Django 3.1.2 on 2020-10-22 05:50

from django.db import migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remember',
            name='coordinate',
            field=geoposition.fields.GeopositionField(max_length=42, verbose_name='Координаты'),
        ),
    ]
