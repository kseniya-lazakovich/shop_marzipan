# Generated by Django 3.0.3 on 2020-03-31 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='imges',
        ),
        migrations.AddField(
            model_name='catalog',
            name='images',
            field=models.CharField(default='default title', max_length=30, verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.CharField(default='default title', max_length=30, verbose_name='Изображение'),
        ),
    ]
