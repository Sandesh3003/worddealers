# Generated by Django 3.2.5 on 2022-04-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20220411_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='number',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='index',
            name='address',
            field=models.CharField(default='', max_length=150),
        ),
    ]