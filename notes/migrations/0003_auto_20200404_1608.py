# Generated by Django 3.0.5 on 2020-04-04 14:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20200404_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='created_note',
        ),
        migrations.AddField(
            model_name='notes',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 4, 14, 8, 58, 524190, tzinfo=utc), verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='content_note',
            field=models.TextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='title_note',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
    ]