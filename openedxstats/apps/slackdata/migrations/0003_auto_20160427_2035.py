# Generated by Django 1.9.5 on 2016-04-27 20:35
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slackdata', '0002_auto_20160427_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagecountbyday',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
