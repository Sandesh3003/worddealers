# Generated by Django 3.2.5 on 2022-04-16 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20220416_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='testimonial')),
                ('facebook_link', models.TextField(max_length=100)),
                ('twitter_link', models.TextField(max_length=100)),
                ('linkedin_link', models.TextField(max_length=100)),
                ('instagram_link', models.TextField(max_length=100)),
            ],
        ),
    ]
