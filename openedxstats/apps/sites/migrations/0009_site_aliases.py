# Generated by Django 1.9.5 on 2017-09-25 20:43
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0008_auto_20160802_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='aliases',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, default=list, size=None),
        ),
    ]
