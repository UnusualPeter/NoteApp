# Generated by Django 3.0.5 on 2020-04-05 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20200404_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Date published'),
        ),
    ]